# Introduction
This repository proprose a template of ddd architecture with Python. It could already be used but it is still in progress. If you have some propsosition please don't hesitate.

# Architecture
In software development, the domain driven design approach is used for complex needs, connecting the implementation to an evolving model of the core business concepts. It puts the focus on the problem domain and basically helps identify the architecture and inform about the mechanics that the software needs to replicate.
DDD has a strategic value and it’s about mapping business domain concepts into software artifacts. It’s about organizing code artifacts in alignment with business problems, using the same common, ubiquitous language.
DDD isn’t a methodology, it’s more about the software’s architectural design, providing a structure of practices to take design decisions that help in software projects that have complicated domains [https://apiumhub.com/tech-blog-barcelona/introduction-domain-driven-design/].

# Front: Vue
The front of the application use Vue. Why Vue? Because Vue is a progressive framework for building user interfaces. Unlike other monolithic frameworks, Vue is designed from the ground up to be incrementally adoptable. The core library is focused on the view layer only, and is easy to pick up and integrate with other libraries or existing projects. On the other hand, Vue is also perfectly capable of powering sophisticated Single-Page Applications when used in combination with modern tooling and supporting libraries [https://vuejs.org/v2/guide/].

After modification Run
```javascript
npm run build
```
This will minify and move the files in the good place on the server.

# Backend: Flask
The back of the application use Flask. Why Flask? Because Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications[https://palletsprojects.com/p/flask/].

Go to localhost:5003/swagger to test the Api. If you change the Api, update the swagger.json file in the Common folder.
Adapt the connection string if youn dont want to use the Fake data.

# Deployment: Ansible
First of all do theses modifications
<ul>
<li>create a main.yml file under secrets and add theses information</li> 
  
```javascript
  azure_client_id: xxxxxxxxxx
  azure_secret: xxxxxxxxxxxxxx
  azure_tenant_id:  xxxxxxxxxxxx
  azure_subscription_id:  xxxxxxxxxxxx
```
To find the values please follow this document: https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal
After modification 
```javascript
run ansible-vault encrypt secrets/main.yml
```
<li>After that you have to give right to the app registration.  Go the "Subscription" menu, then " Access control (IAM)" option. then click on "Add Role"
When it is done go to DevOp folder and run</li>
<li> To deploy run
```javascript
ansible-playbook main.yml -i inventories/servers.yml  --ask-vault-pass 
```
</li>
</ul>


