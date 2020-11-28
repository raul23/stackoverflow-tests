import ipdb


# Question @ https://stackoverflow.com/q/64899771/14664104
# Get max price for each user, see the DataFrame sample `df`
def q1_():
    import pandas as pd

    df = pd.DataFrame([[123, 'xt23', 20],
                       [123, 'q45', 2],
                       [123, 'a89', 25],
                       [77, 'q45', 3],
                       [77, 'a89', 30],
                       [92, 'xt23', 24],
                       [92, 'm33', 60],
                       [92, 'a89', 28]], columns=['userid', 'product', 'price'])

    # User1's answer
    print("***Answer 1***")
    idx = df.groupby(['userid'])['price'].transform(max) == df['price']
    print(df[idx])

    print()

    # User2's answer
    print("***Answer 2***")
    print(df.loc[df.groupby('userid')['price'].idxmax().values, :].sort_index())


if __name__ == '__main__':
    q1_()
