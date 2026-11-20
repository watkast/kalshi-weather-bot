# Range-Scalp Bot

*Updated Fri Nov 20 23:02 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 66647 | 58162 | 8485 (128) | 4 | $-17945.66 | -4.3% |
| **+10¢** | 49772 | 39855 | 9917 (170) | 4 | $-16686.78 | -5.3% |
| **+15¢** | 41739 | 31047 | 10692 (217) | 4 | $-14994.44 | -5.7% |
| **+20¢** | 37158 | 25929 | 11229 (273) | 4 | $-13276.50 | -5.7% |
| **+10¢ (15¢ stop)** | 81162 | 80996 | 166 (100) | 2 | $-29985.06 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-20 23:02 | +10 stop | ZEC | UP | 0.71 | open |  |
| 11-20 23:02 | +20 | ZEC | UP | 0.71 | open |  |
| 11-20 23:02 | +15 | ZEC | UP | 0.71 | open |  |
| 11-20 23:02 | +10 | ZEC | UP | 0.71 | open |  |
| 11-20 23:02 | +5 | ZEC | UP | 0.71 | open |  |
| 11-20 23:01 | +10 stop | BTC | UP | 0.54 | open |  |
| 11-20 23:01 | +20 | BTC | UP | 0.54 | open |  |
| 11-20 23:01 | +15 | BTC | UP | 0.54 | open |  |
| 11-20 23:01 | +10 | BTC | UP | 0.54 | open |  |
| 11-20 23:01 | +5 | BTC | UP | 0.54 | open |  |
| 11-20 23:00 | +10 stop | ETH | DOWN | 0.54 | 0.37 | -2.05 |
| 11-20 23:00 | +20 | ETH | DOWN | 0.54 | open |  |
| 11-20 23:00 | +15 | ETH | DOWN | 0.54 | open |  |
| 11-20 23:00 | +10 | ETH | DOWN | 0.55 | open |  |
| 11-20 23:00 | +5 | ETH | DOWN | 0.55 | open |  |
| 11-20 23:00 | +10 stop | DOGE | DOWN | 0.53 | 0.33 | -2.34 |
| 11-20 23:00 | +20 | DOGE | DOWN | 0.53 | open |  |
| 11-20 23:00 | +15 | DOGE | DOWN | 0.53 | open |  |
| 11-20 23:00 | +10 | DOGE | DOWN | 0.53 | open |  |
| 11-20 23:00 | +5 | DOGE | DOWN | 0.53 | open |  |
| 11-20 22:57 | +5 | HYPE | DOWN | 0.56 | 0.65 | 0.60 |
| 11-20 22:56 | +10 stop | DOGE | DOWN | 0.68 | 0.35 | -3.62 |
| 11-20 22:56 | +10 | DOGE | DOWN | 0.68 | yes | -6.96 |
| 11-20 22:56 | +5 | DOGE | DOWN | 0.68 | yes | -6.96 |
| 11-20 22:56 | +10 stop | NEAR | DOWN | 0.67 | 0.79 | 0.92 |
| 11-20 22:56 | +15 | NEAR | DOWN | 0.67 | 0.82 | 1.23 |
| 11-20 22:56 | +10 | NEAR | DOWN | 0.67 | 0.79 | 0.92 |
| 11-20 22:56 | +5 | NEAR | DOWN | 0.67 | 0.79 | 0.92 |
| 11-20 22:55 | +10 stop | DOGE | DOWN | 0.55 | 0.68 | 0.96 |
| 11-20 22:55 | +20 | DOGE | DOWN | 0.55 | yes | -5.68 |
| 11-20 22:55 | +15 | DOGE | DOWN | 0.55 | 0.70 | 1.17 |
| 11-20 22:55 | +10 | DOGE | DOWN | 0.55 | 0.68 | 0.96 |
| 11-20 22:55 | +5 | DOGE | DOWN | 0.55 | 0.68 | 0.96 |
| 11-20 22:55 | +10 stop | HYPE | DOWN | 0.56 | 0.66 | 0.66 |
| 11-20 22:55 | +20 | HYPE | DOWN | 0.56 | 0.76 | 1.69 |
| 11-20 22:55 | +15 | HYPE | DOWN | 0.56 | 0.76 | 1.69 |
| 11-20 22:55 | +10 | HYPE | DOWN | 0.56 | 0.66 | 0.66 |
| 11-20 22:55 | +5 | HYPE | DOWN | 0.56 | 0.63 | 0.35 |
| 11-20 22:53 | +10 stop | NEAR | DOWN | 0.66 | 0.82 | 1.33 |
| 11-20 22:53 | +15 | NEAR | DOWN | 0.66 | 0.82 | 1.33 |
