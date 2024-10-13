from sklearn.cluster import KMeans

class TeamAssigner:
    def __init__(self):
        self.team_colors = {}
        self.player_team_dict = {}

    def get_clustering_model(self, image):
        # Reshape the image to a 2D array where each row represents a pixel and each column represents a color channel (R, G, B)
        image_2d = image.reshape(-1, 3)

        # Perform K-means clustering with 2 clusters to separate the image into two dominant colors
        kmeans = KMeans(n_clusters=2, init="k-means++", n_init=1)
        kmeans.fit(image_2d)

        # Return the trained K-means model
        return kmeans

    def get_player_color(self, frame, bbox):
        # Extract the region of interest (ROI) from the frame using the bounding box coordinates
        image = frame[int(bbox[1]):int(bbox[3]), int(bbox[0]):int(bbox[2])]

        # Use the top half of the extracted image for clustering to avoid including shorts or other non-jersey parts
        top_half_image = image[0:int(image.shape[0] / 2), :]

        # Get the clustering model for the top half of the image
        kmeans = self.get_clustering_model(top_half_image)

        # Get the cluster labels for each pixel in the top half image
        labels = kmeans.labels_

        # Reshape the labels to match the shape of the top half image
        clustered_image = labels.reshape(top_half_image.shape[0], top_half_image.shape[1])

        # Determine the cluster that represents the player's jersey color by examining the corners of the image
        corner_clusters = [clustered_image[0, 0], clustered_image[0, -1], clustered_image[-1, 0], clustered_image[-1, -1]]
        non_player_cluster = max(set(corner_clusters), key=corner_clusters.count)
        player_cluster = 1 - non_player_cluster

        # Get the color of the player's jersey from the cluster centers
        player_color = kmeans.cluster_centers_[player_cluster]

        return player_color

    def assign_team_color(self, frame, player_detections):
        player_colors = []
        for _, player_detection in player_detections.items():
            bbox = player_detection["bbox"]
            player_color = self.get_player_color(frame, bbox)
            player_colors.append(player_color)

        # Perform K-means clustering on the collected player colors to separate them into two teams
        kmeans = KMeans(n_clusters=2, init="k-means++", n_init=10)
        kmeans.fit(player_colors)

        self.kmeans = kmeans

        # Assign team colors based on the cluster centers obtained from K-means clustering
        self.team_colors[1] = kmeans.cluster_centers_[0]
        self.team_colors[2] = kmeans.cluster_centers_[1]

    def get_player_team(self, frame, player_bbox, player_id):
        # Check if the player's team has already been determined
        if player_id in self.player_team_dict:
            return self.player_team_dict[player_id]

        # Get the color of the player's jersey
        player_color = self.get_player_color(frame, player_bbox)

        # Predict the team ID based on the player's jersey color using the trained K-means model
        team_id = self.kmeans.predict(player_color.reshape(1, -1))[0]
        team_id += 1

        # Special case for player ID 91, always assign to team 1
        if player_id == 91:
            team_id = 1

        # Store the player's team ID in the dictionary
        self.player_team_dict[player_id] = team_id

        return team_id
