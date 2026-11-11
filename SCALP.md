# Range-Scalp Bot

*Updated Wed Nov 11 06:50 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 55557 | 48452 | 7105 (94) | 7 | $-15176.95 | -4.3% |
| **+10¢** | 41508 | 33218 | 8290 (124) | 7 | $-14123.44 | -5.4% |
| **+15¢** | 34802 | 25862 | 8940 (158) | 8 | $-12887.27 | -5.9% |
| **+20¢** | 30994 | 21617 | 9377 (207) | 8 | $-11265.99 | -5.8% |
| **+10¢ (15¢ stop)** | 67663 | 67545 | 118 (73) | 3 | $-24915.74 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 06:50 | +5 | ZEC | UP | 0.54 | 0.59 | 0.15 |
| 11-11 06:50 | +10 stop | ZEC | UP | 0.54 | 0.66 | 0.86 |
| 11-11 06:49 | +5 | NEAR | DOWN | 0.70 | open |  |
| 11-11 06:49 | +10 stop | HYPE | DOWN | 0.62 | 0.43 | -2.25 |
| 11-11 06:48 | +10 stop | XRP | DOWN | 0.61 | open |  |
| 11-11 06:48 | +10 | XRP | DOWN | 0.61 | open |  |
| 11-11 06:48 | +10 stop | DOGE | DOWN | 0.71 | open |  |
| 11-11 06:48 | +10 stop | ZEC | DOWN | 0.66 | 0.49 | -2.04 |
| 11-11 06:48 | +10 stop | SOL | DOWN | 0.69 | open |  |
| 11-11 06:48 | +20 | SOL | DOWN | 0.69 | open |  |
| 11-11 06:48 | +10 stop | XRP | UP | 0.44 | 0.56 | 0.84 |
| 11-11 06:48 | +10 | XRP | UP | 0.44 | 0.56 | 0.84 |
| 11-11 06:48 | +10 stop | NEAR | DOWN | 0.67 | 0.47 | -2.34 |
| 11-11 06:48 | +20 | NEAR | DOWN | 0.66 | open |  |
| 11-11 06:48 | +15 | NEAR | DOWN | 0.66 | open |  |
| 11-11 06:48 | +10 | NEAR | DOWN | 0.66 | open |  |
| 11-11 06:48 | +5 | NEAR | DOWN | 0.67 | 0.73 | 0.30 |
| 11-11 06:47 | +10 stop | HYPE | UP | 0.51 | 0.69 | 1.47 |
| 11-11 06:47 | +10 stop | ZEC | UP | 0.57 | 0.37 | -2.35 |
| 11-11 06:47 | +20 | ZEC | UP | 0.57 | open |  |
| 11-11 06:47 | +15 | ZEC | UP | 0.56 | open |  |
| 11-11 06:47 | +10 | ZEC | UP | 0.56 | 0.66 | 0.66 |
| 11-11 06:47 | +5 | ZEC | UP | 0.56 | 0.63 | 0.35 |
| 11-11 06:47 | +5 | XRP | UP | 0.68 | open |  |
| 11-11 06:47 | +10 stop | DOGE | UP | 0.60 | 0.37 | -2.64 |
| 11-11 06:47 | +10 | DOGE | UP | 0.60 | open |  |
| 11-11 06:47 | +5 | DOGE | UP | 0.60 | open |  |
| 11-11 06:47 | +5 | SOL | UP | 0.60 | open |  |
| 11-11 06:46 | +10 stop | XRP | UP | 0.57 | 0.67 | 0.66 |
| 11-11 06:46 | +20 | XRP | UP | 0.57 | open |  |
| 11-11 06:46 | +15 | XRP | UP | 0.57 | open |  |
| 11-11 06:46 | +10 | XRP | UP | 0.57 | 0.67 | 0.66 |
| 11-11 06:46 | +5 | XRP | UP | 0.57 | 0.62 | 0.15 |
| 11-11 06:46 | +10 stop | DOGE | UP | 0.52 | 0.65 | 0.96 |
| 11-11 06:46 | +20 | DOGE | UP | 0.52 | open |  |
| 11-11 06:46 | +15 | DOGE | UP | 0.52 | open |  |
| 11-11 06:46 | +10 | DOGE | UP | 0.52 | 0.65 | 0.96 |
| 11-11 06:46 | +5 | DOGE | UP | 0.52 | 0.65 | 0.96 |
| 11-11 06:46 | +10 stop | SOL | UP | 0.52 | 0.34 | -2.14 |
| 11-11 06:46 | +15 | SOL | UP | 0.53 | open |  |
