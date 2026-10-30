# Range-Scalp Bot

*Updated Fri Oct 30 11:23 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 40657 | 35485 | 5172 (51) | 6 | $-11363.87 | -4.4% |
| **+10¢** | 30295 | 24314 | 5981 (74) | 6 | $-10119.11 | -5.3% |
| **+15¢** | 25333 | 18894 | 6439 (101) | 6 | $-9141.97 | -5.7% |
| **+20¢** | 22484 | 15733 | 6751 (131) | 6 | $-8078.53 | -5.7% |
| **+10¢ (15¢ stop)** | 49583 | 49513 | 70 (37) | 5 | $-18770.08 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-30 11:23 | +5 | ZEC | DOWN | 0.68 | open |  |
| 10-30 11:22 | +10 stop | DOGE | DOWN | 0.63 | open |  |
| 10-30 11:22 | +10 stop | SOL | DOWN | 0.66 | open |  |
| 10-30 11:22 | +10 stop | DOGE | DOWN | 0.44 | 0.54 | 0.64 |
| 10-30 11:22 | +10 stop | BTC | UP | 0.62 | open |  |
| 10-30 11:22 | +10 stop | ETH | UP | 0.68 | open |  |
| 10-30 11:22 | +5 | ZEC | DOWN | 0.62 | 0.67 | 0.17 |
| 10-30 11:21 | +10 stop | ZEC | DOWN | 0.63 | open |  |
| 10-30 11:21 | +10 stop | SOL | UP | 0.46 | 0.58 | 0.84 |
| 10-30 11:21 | +10 stop | NEAR | DOWN | 0.66 | 0.76 | 0.71 |
| 10-30 11:21 | +10 | NEAR | DOWN | 0.66 | 0.76 | 0.71 |
| 10-30 11:21 | +5 | NEAR | DOWN | 0.66 | 0.76 | 0.71 |
| 10-30 11:20 | +10 stop | BTC | UP | 0.64 | 0.78 | 1.10 |
| 10-30 11:20 | +5 | ZEC | DOWN | 0.61 | 0.67 | 0.27 |
| 10-30 11:19 | +10 stop | SOL | DOWN | 0.56 | 0.32 | -2.74 |
| 10-30 11:19 | +10 stop | ETH | DOWN | 0.60 | 0.43 | -2.05 |
| 10-30 11:19 | +5 | ETH | DOWN | 0.60 | open |  |
| 10-30 11:19 | +10 stop | BTC | DOWN | 0.58 | 0.38 | -2.35 |
| 10-30 11:19 | +10 stop | DOGE | DOWN | 0.66 | 0.46 | -2.34 |
| 10-30 11:19 | +20 | DOGE | DOWN | 0.66 | open |  |
| 10-30 11:19 | +15 | DOGE | DOWN | 0.66 | open |  |
| 10-30 11:19 | +10 | DOGE | DOWN | 0.66 | open |  |
| 10-30 11:19 | +5 | DOGE | DOWN | 0.66 | open |  |
| 10-30 11:18 | +10 stop | SOL | DOWN | 0.52 | 0.64 | 0.85 |
| 10-30 11:17 | +10 stop | ZEC | DOWN | 0.66 | 0.51 | -1.84 |
| 10-30 11:17 | +10 | ZEC | DOWN | 0.66 | open |  |
| 10-30 11:17 | +5 | ZEC | DOWN | 0.66 | 0.72 | 0.29 |
| 10-30 11:17 | +10 stop | ETH | DOWN | 0.61 | 0.46 | -1.85 |
| 10-30 11:17 | +20 | ETH | DOWN | 0.61 | open |  |
| 10-30 11:17 | +15 | ETH | DOWN | 0.61 | open |  |
| 10-30 11:17 | +10 | ETH | DOWN | 0.61 | open |  |
| 10-30 11:17 | +5 | ETH | DOWN | 0.61 | 0.67 | 0.27 |
| 10-30 11:16 | +10 stop | SOL | DOWN | 0.67 | 0.49 | -2.14 |
| 10-30 11:16 | +20 | SOL | DOWN | 0.67 | open |  |
| 10-30 11:16 | +15 | SOL | DOWN | 0.67 | open |  |
| 10-30 11:16 | +10 | SOL | DOWN | 0.67 | open |  |
| 10-30 11:16 | +5 | SOL | DOWN | 0.67 | open |  |
| 10-30 11:16 | +10 stop | BNB | DOWN | 0.57 | 0.35 | -2.54 |
| 10-30 11:16 | +20 | BNB | DOWN | 0.58 | open |  |
| 10-30 11:16 | +15 | BNB | DOWN | 0.57 | open |  |
