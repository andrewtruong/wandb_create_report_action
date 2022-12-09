import wandb.apis.reports as wr

report = wr.Report(
    project='github-actions-report',
    blocks=[
        wr.H1('This report was generated from a github action.'),
        wr.P("To learn more, check out the repo at ...")
    ]
).save()

print(report.url)