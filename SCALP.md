# Range-Scalp Bot

*Updated Fri Oct 23 15:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 30569 | 26634 | 3935 (39) | 5 | $-8869.16 | -4.6% |
| **+10¢** | 22875 | 18323 | 4552 (56) | 6 | $-7932.02 | -5.5% |
| **+15¢** | 19143 | 14249 | 4894 (79) | 7 | $-7131.77 | -5.9% |
| **+20¢** | 16953 | 11826 | 5127 (102) | 7 | $-6398.82 | -6.0% |
| **+10¢ (15¢ stop)** | 37476 | 37417 | 59 (32) | 2 | $-14214.03 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 15:40 | +10 stop | ZEC | UP | 0.65 | 0.76 | 0.81 |
| 10-23 15:40 | +20 | ZEC | UP | 0.65 | open |  |
| 10-23 15:40 | +15 | ZEC | UP | 0.64 | open |  |
| 10-23 15:40 | +10 | ZEC | UP | 0.64 | 0.76 | 0.90 |
| 10-23 15:39 | +10 stop | ETH | DOWN | 0.68 | open |  |
| 10-23 15:38 | +5 | ZEC | UP | 0.69 | 0.76 | 0.42 |
| 10-23 15:38 | +10 stop | BTC | DOWN | 0.63 | 0.48 | -1.85 |
| 10-23 15:38 | +10 | BTC | DOWN | 0.63 | open |  |
| 10-23 15:38 | +5 | BTC | DOWN | 0.63 | open |  |
| 10-23 15:37 | +10 stop | SOL | DOWN | 0.70 | 0.50 | -2.33 |
| 10-23 15:37 | +10 | SOL | DOWN | 0.70 | open |  |
| 10-23 15:37 | +5 | SOL | DOWN | 0.70 | open |  |
| 10-23 15:37 | +10 stop | ZEC | UP | 0.50 | 0.61 | 0.75 |
| 10-23 15:37 | +20 | ZEC | UP | 0.50 | 0.73 | 1.98 |
| 10-23 15:37 | +15 | ZEC | UP | 0.50 | 0.73 | 1.98 |
| 10-23 15:37 | +10 | ZEC | UP | 0.50 | 0.61 | 0.75 |
| 10-23 15:37 | +5 | ZEC | UP | 0.50 | 0.55 | 0.14 |
| 10-23 15:37 | +10 stop | BNB | DOWN | 0.64 | open |  |
| 10-23 15:37 | +5 | BNB | DOWN | 0.64 | open |  |
| 10-23 15:36 | +10 stop | HYPE | DOWN | 0.56 | 0.71 | 1.17 |
| 10-23 15:36 | +10 stop | XRP | DOWN | 0.62 | 0.76 | 1.10 |
| 10-23 15:36 | +5 | ETH | UP | 0.61 | open |  |
| 10-23 15:36 | +10 stop | DOGE | UP | 0.66 | 0.46 | -2.34 |
| 10-23 15:36 | +10 stop | XRP | UP | 0.71 | 0.45 | -2.93 |
| 10-23 15:35 | +10 stop | ETH | UP | 0.64 | 0.47 | -2.05 |
| 10-23 15:35 | +5 | ETH | UP | 0.62 | 0.67 | 0.17 |
| 10-23 15:34 | +10 stop | BTC | UP | 0.59 | 0.73 | 1.09 |
| 10-23 15:34 | +10 stop | ZEC | DOWN | 0.52 | 0.34 | -2.14 |
| 10-23 15:33 | +10 stop | ETH | DOWN | 0.55 | 0.36 | -2.25 |
| 10-23 15:33 | +10 stop | BNB | DOWN | 0.60 | 0.38 | -2.53 |
| 10-23 15:33 | +10 stop | XRP | DOWN | 0.56 | 0.32 | -2.74 |
| 10-23 15:33 | +10 stop | NEAR | DOWN | 0.66 | 0.49 | -2.04 |
| 10-23 15:33 | +20 | NEAR | DOWN | 0.66 | 0.89 | 2.07 |
| 10-23 15:33 | +15 | NEAR | DOWN | 0.66 | 0.82 | 1.33 |
| 10-23 15:33 | +10 | NEAR | DOWN | 0.66 | 0.82 | 1.33 |
| 10-23 15:33 | +5 | NEAR | DOWN | 0.66 | 0.73 | 0.40 |
| 10-23 15:33 | +10 stop | DOGE | DOWN | 0.61 | 0.44 | -2.05 |
| 10-23 15:33 | +20 | DOGE | DOWN | 0.61 | 0.81 | 1.72 |
| 10-23 15:33 | +15 | DOGE | DOWN | 0.61 | 0.81 | 1.72 |
| 10-23 15:33 | +10 | DOGE | DOWN | 0.61 | 0.75 | 1.09 |
