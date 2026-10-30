# Range-Scalp Bot

*Updated Fri Oct 30 18:32 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 41110 | 35885 | 5225 (53) | 2 | $-11451.86 | -4.4% |
| **+10¢** | 30638 | 24594 | 6044 (76) | 3 | $-10176.70 | -5.3% |
| **+15¢** | 25612 | 19100 | 6512 (103) | 4 | $-9230.04 | -5.7% |
| **+20¢** | 22732 | 15910 | 6822 (133) | 6 | $-8128.53 | -5.7% |
| **+10¢ (15¢ stop)** | 50124 | 50054 | 70 (37) | 1 | $-18939.23 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-30 18:31 | +10 stop | XRP | UP | 0.37 | 0.53 | 1.25 |
| 10-30 18:31 | +20 | XRP | UP | 0.37 | open |  |
| 10-30 18:31 | +15 | XRP | UP | 0.37 | 0.53 | 1.25 |
| 10-30 18:31 | +10 | XRP | UP | 0.37 | 0.53 | 1.25 |
| 10-30 18:31 | +5 | XRP | UP | 0.37 | 0.53 | 1.25 |
| 10-30 18:31 | +10 stop | BNB | UP | 0.57 | 0.36 | -2.45 |
| 10-30 18:31 | +20 | BNB | UP | 0.57 | open |  |
| 10-30 18:31 | +15 | BNB | UP | 0.57 | open |  |
| 10-30 18:31 | +10 | BNB | UP | 0.58 | open |  |
| 10-30 18:31 | +5 | BNB | UP | 0.59 | open |  |
| 10-30 18:31 | +10 stop | ETH | UP | 0.59 | 0.38 | -2.44 |
| 10-30 18:31 | +20 | ETH | UP | 0.59 | open |  |
| 10-30 18:31 | +15 | ETH | UP | 0.59 | open |  |
| 10-30 18:31 | +10 | ETH | UP | 0.59 | open |  |
| 10-30 18:31 | +5 | ETH | UP | 0.59 | open |  |
| 10-30 18:31 | +10 stop | ZEC | DOWN | 0.60 | open |  |
| 10-30 18:31 | +20 | ZEC | DOWN | 0.62 | open |  |
| 10-30 18:31 | +15 | ZEC | DOWN | 0.62 | open |  |
| 10-30 18:31 | +10 | ZEC | DOWN | 0.62 | open |  |
| 10-30 18:31 | +5 | ZEC | DOWN | 0.62 | 0.67 | 0.17 |
| 10-30 18:31 | +10 stop | NEAR | DOWN | 0.61 | 0.71 | 0.68 |
| 10-30 18:31 | +20 | NEAR | DOWN | 0.61 | open |  |
| 10-30 18:31 | +15 | NEAR | DOWN | 0.61 | open |  |
| 10-30 18:31 | +10 | NEAR | DOWN | 0.61 | 0.71 | 0.68 |
| 10-30 18:31 | +5 | NEAR | DOWN | 0.61 | 0.71 | 0.68 |
| 10-30 18:31 | +10 stop | HYPE | DOWN | 0.62 | 0.78 | 1.30 |
| 10-30 18:31 | +20 | HYPE | DOWN | 0.62 | open |  |
| 10-30 18:31 | +15 | HYPE | DOWN | 0.62 | 0.78 | 1.30 |
| 10-30 18:31 | +10 | HYPE | DOWN | 0.62 | 0.78 | 1.30 |
| 10-30 18:31 | +5 | HYPE | DOWN | 0.62 | 0.78 | 1.30 |
| 10-30 18:20 | +10 stop | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 10-30 18:20 | +15 | NEAR | DOWN | 0.70 | 0.89 | 1.68 |
| 10-30 18:20 | +10 | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 10-30 18:20 | +5 | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 10-30 18:17 | +15 | BNB | DOWN | 0.70 | 0.85 | 1.26 |
| 10-30 18:17 | +10 stop | BNB | DOWN | 0.71 | 0.81 | 0.74 |
| 10-30 18:17 | +20 | BNB | DOWN | 0.71 | 0.94 | 2.14 |
| 10-30 18:17 | +10 | BNB | DOWN | 0.69 | 0.79 | 0.73 |
| 10-30 18:17 | +5 | BNB | DOWN | 0.68 | 0.73 | 0.20 |
| 10-30 18:17 | +10 stop | NEAR | DOWN | 0.64 | 0.75 | 0.79 |
