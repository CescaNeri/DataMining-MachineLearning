# Customer Retention 

Customer retention, churn analysis, dropout analysis are synonyms for predictive analysis carried out by organizations and companies to avoid losing customers.

The idea is to create a different profile for customers who stay and customers who drop-out.

**The Gym Case Study**

They discovered that customers who did not train well, eventually drop out from the gym.
Therefore, the goal was to model customers' training sessions in order to predict those who did not train well and prevent them from dropping out.

Steps:

- Customers have s list of exercises
- The system records the exercises (and repetition) did during the workout
- The system matches the exercises 
- Train a classifier that is able to predict that someone is leaving the gym because he is unsatisfied
    - The system update the profile each week
    - Four weeks without training = dropout
    - The idea of dropout needs to be defined properly (a customer who stops going to the gym in summer and comes back in summer is different from a customers who dropout and does not come back)

Practitioner who is about to leave the gym is training poorly. How can characterize the user behaviors? How long does it last?

Many KPIs can be adopted to assess the training session: in this case, two indicators were identified:

1. **Compliance** (adherence of the performed workout)
2. **Regularity** (regularity of the training sessions with reference to the prescribed one)

We still have a problem of **granularity:** we can assess regularity by checking steps, repetition, physical activity, muscle or body part. 



