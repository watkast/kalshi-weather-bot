# Range-Scalp Bot

*Updated Thu Oct 08 10:51 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 7452 | 6453 | 999 (13) | 2 | $-2353.96 | -5.0% |
| **+10¢** | 5661 | 4481 | 1180 (22) | 2 | $-2313.01 | -6.5% |
| **+15¢** | 4750 | 3508 | 1242 (30) | 2 | $-1918.98 | -6.4% |
| **+20¢** | 4241 | 2953 | 1288 (37) | 2 | $-1531.86 | -5.8% |
| **+10¢ (15¢ stop)** | 9041 | 9014 | 27 (17) | 1 | $-3277.69 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-08 10:50 | +10 stop | ETH | DOWN | 0.67 | 0.79 | 0.92 |
| 10-08 10:50 | +10 stop | BTC | DOWN | 0.59 | open |  |
| 10-08 10:47 | +10 stop | BTC | DOWN | 0.65 | 0.76 | 0.81 |
| 10-08 10:46 | +10 stop | SOL | DOWN | 0.64 | 0.75 | 0.79 |
| 10-08 10:46 | +20 | SOL | DOWN | 0.64 | 0.85 | 1.84 |
| 10-08 10:46 | +15 | SOL | DOWN | 0.64 | 0.81 | 1.42 |
| 10-08 10:46 | +10 | SOL | DOWN | 0.64 | 0.75 | 0.79 |
| 10-08 10:46 | +5 | SOL | DOWN | 0.64 | 0.71 | 0.38 |
| 10-08 10:46 | +10 stop | BNB | DOWN | 0.61 | 0.76 | 1.20 |
| 10-08 10:46 | +20 | BNB | DOWN | 0.61 | 0.84 | 2.03 |
| 10-08 10:46 | +15 | BNB | DOWN | 0.61 | 0.76 | 1.20 |
| 10-08 10:46 | +10 | BNB | DOWN | 0.61 | 0.76 | 1.20 |
| 10-08 10:46 | +5 | BNB | DOWN | 0.61 | 0.76 | 1.20 |
| 10-08 10:46 | +10 stop | HYPE | DOWN | 0.65 | 0.78 | 0.97 |
| 10-08 10:46 | +20 | HYPE | DOWN | 0.65 | 0.92 | 2.48 |
| 10-08 10:46 | +15 | HYPE | DOWN | 0.66 | 0.84 | 1.50 |
| 10-08 10:46 | +10 | HYPE | DOWN | 0.65 | 0.78 | 1.01 |
| 10-08 10:46 | +5 | HYPE | DOWN | 0.65 | 0.70 | 0.19 |
| 10-08 10:46 | +10 stop | DOGE | DOWN | 0.63 | 0.76 | 1.00 |
| 10-08 10:46 | +20 | DOGE | DOWN | 0.63 | 0.90 | 2.48 |
| 10-08 10:46 | +15 | DOGE | DOWN | 0.63 | 0.90 | 2.48 |
| 10-08 10:46 | +10 | DOGE | DOWN | 0.63 | 0.76 | 1.00 |
| 10-08 10:46 | +5 | DOGE | DOWN | 0.63 | 0.69 | 0.28 |
| 10-08 10:46 | +10 stop | ETH | UP | 0.64 | 0.47 | -2.05 |
| 10-08 10:46 | +20 | ETH | UP | 0.64 | open |  |
| 10-08 10:46 | +15 | ETH | UP | 0.64 | open |  |
| 10-08 10:46 | +10 | ETH | UP | 0.64 | open |  |
| 10-08 10:46 | +5 | ETH | UP | 0.64 | open |  |
| 10-08 10:46 | +10 stop | BTC | UP | 0.57 | 0.40 | -2.05 |
| 10-08 10:46 | +20 | BTC | UP | 0.57 | open |  |
| 10-08 10:46 | +15 | BTC | UP | 0.57 | open |  |
| 10-08 10:46 | +10 | BTC | UP | 0.57 | open |  |
| 10-08 10:46 | +5 | BTC | UP | 0.57 | open |  |
| 10-08 10:37 | +10 stop | SOL | DOWN | 0.69 | 0.81 | 0.94 |
| 10-08 10:37 | +15 | SOL | DOWN | 0.69 | 0.89 | 1.78 |
| 10-08 10:36 | +5 | SOL | UP | 0.61 | no | -6.27 |
| 10-08 10:36 | +10 stop | SOL | UP | 0.64 | 0.40 | -2.74 |
| 10-08 10:36 | +20 | SOL | UP | 0.64 | no | -6.57 |
| 10-08 10:36 | +10 | SOL | UP | 0.64 | no | -6.57 |
| 10-08 10:36 | +5 | SOL | UP | 0.58 | 0.67 | 0.56 |
