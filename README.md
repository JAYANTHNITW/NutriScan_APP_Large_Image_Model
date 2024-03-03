# NutriScan App
 
| <img src="d5e4b9404ae867206c2945b4f51186e4.jpg" width="400"/> | <img src="Screenshot 2024-01-30 195300.png" width="400"/> |

**Overview:**

- NutriScan is a user-friendly nutritional analysis app designed for individuals, including college students, to make informed dietary choices.
- The app utilizes advanced image recognition technology to analyze food items, providing detailed nutritional information for each item.

**Key Features:**

- **Image Recognition:**
  - Upload images of food items, and NutriScan will identify and analyze them using advanced image recognition algorithms.

- **Detailed Nutritional Analysis:**
  - Receive a comprehensive breakdown of nutritional components, including calories, proteins, carbohydrates, fibers, and fats for each food item.

- **Daily Intake Recommendations:**
  - The app offers daily macronutrient intake recommendations based on general guidelines, taking into account calories, proteins, carbohydrates, and fats.

- **User-Friendly Interface:**
  - An intuitive and user-friendly interface makes it easy for users to understand and interpret nutritional information.

**How to Use:**

1. **Upload Image:**
   - Simply upload an image of the food item you want to analyze.

2. **View Nutritional Details:**
   - NutriScan will generate a detailed table presenting the nutritional content of the food item, helping users make informed dietary choices.

3. **Daily Intake Guidelines:**
   - Get an overview of your daily macronutrient intake recommendations based on standard guidelines.

**Installation:**

- Clone this repository.
- Install the required dependencies using the provided `requirements.txt` file.
- Run the app locally or deploy it on a web server for public access.

**Dependencies:**

- [List of dependencies]

**Contribute:**

- Contributions to the development of NutriScan are welcome!
- Feel free to fork the repository, make improvements, and submit pull requests.

**License:**

- This app is licensed under [License Name].
- See the [LICENSE](LICENSE) file for details.

- ## Project Setup

### Prerequisites
- A Google Cloud Platform (GCP) project
- A GitHub repository containing your application code

### Deployment Instructions

#### 1. Dockerfile

1. Create a Dockerfile in the root of your project directory.

Example (basic Python app):
```
Dockerfile
FROM python:3.9

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY 

EXPOSE 8080

CMD ["python", "app.py"]
```
#### 2. cloudbuild.yaml
Create a cloudbuild.yaml file in your project's root directory.
Example:
steps:
```
- name: 'gcr.io/cloud-builders/docker'
  args: ['build', '-t', 'gcr.io/$PROJECT_ID/your-app-name', '.']
- name: 'gcr.io/cloud-builders/docker'
  args: ['push', 'gcr.io/$PROJECT_ID/your-app-name']
- name: 'gcr.io/cloud-builders/gcloud'
  args: ['run', 'deploy', 'your-app-name', '--image', 'gcr.io/$PROJECT_ID/your-app-name', '--region', 'asia-south1', '--platform', 'managed', '--allow-unauthenticated']  
```
 Replace `$PROJECT_ID` with your GCP project ID. Update `your-app-name` as needed.

#### 3. Enable APIs
In the Google Cloud Console, enable the following APIs:
- Cloud Build API
- Cloud Run API
- IAM API
  
#### 4. IAM Permissions
* Grant necessary permissions to the Cloud Build service account:
* Cloud Run Admin
* Storage Object Admin (if needed)

#### 5. Create a Cloud Run Service
* Choose your desired region in the Google Cloud Console.
  
#### 6. Cloud Build Trigger
* Connect your GitHub repository to Cloud Build.
* Create a trigger for your main (or relevant) branch.
  
#### 7. Deployment
* Push changes to your GitHub repository to trigger the deployment process.
  
#### Troubleshooting
- Check build logs in Cloud Build.
- Verify Cloud Build service account permissions.
- Review Cloud Run service configuration.

#### Feel free to reach out with any questions!
