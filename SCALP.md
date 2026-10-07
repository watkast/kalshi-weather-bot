# Range-Scalp Bot

*Updated Wed Oct 07 21:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 6818 | 5920 | 898 (10) | 2 | $-2065.60 | -4.8% |
| **+10¢** | 5175 | 4122 | 1053 (17) | 3 | $-1938.70 | -5.9% |
| **+15¢** | 4336 | 3228 | 1108 (21) | 3 | $-1612.80 | -5.9% |
| **+20¢** | 3875 | 2720 | 1155 (28) | 3 | $-1285.12 | -5.3% |
| **+10¢ (15¢ stop)** | 8265 | 8248 | 17 (10) | 0 | $-2931.73 | -5.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-07 21:08 | +5 | BNB | DOWN | 0.71 | 0.77 | 0.32 |
| 10-07 21:07 | +10 stop | ZEC | DOWN | 0.61 | 0.45 | -1.95 |
| 10-07 21:06 | +10 stop | HYPE | DOWN | 0.55 | 0.40 | -1.85 |
| 10-07 21:05 | +10 stop | BNB | DOWN | 0.71 | 0.89 | 1.59 |
| 10-07 21:05 | +15 | BNB | DOWN | 0.71 | 0.89 | 1.59 |
| 10-07 21:05 | +10 | BNB | DOWN | 0.71 | 0.89 | 1.59 |
| 10-07 21:05 | +5 | BNB | DOWN | 0.71 | 0.76 | 0.23 |
| 10-07 21:05 | +10 stop | XRP | DOWN | 0.67 | 0.78 | 0.81 |
| 10-07 21:05 | +15 | XRP | DOWN | 0.67 | 0.82 | 1.23 |
| 10-07 21:05 | +10 | XRP | DOWN | 0.67 | 0.78 | 0.81 |
| 10-07 21:05 | +5 | XRP | DOWN | 0.67 | 0.72 | 0.19 |
| 10-07 21:05 | +10 stop | ZEC | DOWN | 0.56 | 0.66 | 0.66 |
| 10-07 21:04 | +5 | HYPE | DOWN | 0.56 | 0.68 | 0.86 |
| 10-07 21:04 | +10 stop | HYPE | DOWN | 0.55 | 0.37 | -2.15 |
| 10-07 21:04 | +15 | HYPE | DOWN | 0.55 | 0.70 | 1.17 |
| 10-07 21:04 | +10 | HYPE | DOWN | 0.55 | 0.68 | 0.96 |
| 10-07 21:04 | +5 | HYPE | DOWN | 0.55 | 0.62 | 0.35 |
| 10-07 21:03 | +10 stop | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 10-07 21:03 | +10 stop | HYPE | DOWN | 0.60 | 0.73 | 0.99 |
| 10-07 21:03 | +20 | HYPE | DOWN | 0.60 | 0.88 | 2.55 |
| 10-07 21:03 | +15 | HYPE | DOWN | 0.60 | 0.76 | 1.30 |
| 10-07 21:03 | +10 | HYPE | DOWN | 0.60 | 0.73 | 0.99 |
| 10-07 21:03 | +5 | HYPE | DOWN | 0.59 | 0.73 | 1.09 |
| 10-07 21:02 | +10 stop | BNB | DOWN | 0.61 | 0.72 | 0.75 |
| 10-07 21:02 | +20 | BNB | DOWN | 0.61 | 0.89 | 2.53 |
| 10-07 21:02 | +15 | BNB | DOWN | 0.61 | 0.78 | 1.37 |
| 10-07 21:02 | +10 | BNB | DOWN | 0.61 | 0.72 | 0.75 |
| 10-07 21:02 | +5 | BNB | DOWN | 0.62 | 0.72 | 0.68 |
| 10-07 21:02 | +5 | ZEC | UP | 0.63 | open |  |
| 10-07 21:02 | +5 | SOL | DOWN | 0.70 | 0.78 | 0.52 |
| 10-07 21:02 | +10 stop | NEAR | UP | 0.51 | 0.34 | -2.04 |
| 10-07 21:02 | +20 | NEAR | UP | 0.51 | open |  |
| 10-07 21:02 | +15 | NEAR | UP | 0.52 | open |  |
| 10-07 21:02 | +10 | NEAR | UP | 0.52 | open |  |
| 10-07 21:02 | +5 | NEAR | UP | 0.51 | 0.58 | 0.34 |
| 10-07 21:01 | +10 stop | DOGE | DOWN | 0.66 | 0.77 | 0.81 |
| 10-07 21:01 | +20 | DOGE | DOWN | 0.66 | 0.86 | 1.75 |
| 10-07 21:01 | +15 | DOGE | DOWN | 0.66 | 0.82 | 1.35 |
| 10-07 21:01 | +10 | DOGE | DOWN | 0.65 | 0.77 | 0.90 |
| 10-07 21:01 | +5 | DOGE | DOWN | 0.65 | 0.73 | 0.49 |
