# Range-Scalp Bot

*Updated Tue Oct 13 09:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 14483 | 12519 | 1964 (27) | 1 | $-4720.62 | -5.2% |
| **+10¢** | 10956 | 8676 | 2280 (39) | 1 | $-4441.03 | -6.4% |
| **+15¢** | 9208 | 6770 | 2438 (57) | 1 | $-3954.64 | -6.8% |
| **+20¢** | 8194 | 5655 | 2539 (72) | 1 | $-3414.50 | -6.6% |
| **+10¢ (15¢ stop)** | 17766 | 17717 | 49 (29) | 0 | $-6903.57 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-13 09:57 | +10 stop | ETH | UP | 0.63 | 0.73 | 0.69 |
| 10-13 09:56 | +10 stop | ETH | UP | 0.59 | 0.72 | 0.98 |
| 10-13 09:55 | +5 | BTC | DOWN | 0.59 | 0.80 | 1.81 |
| 10-13 09:54 | +10 stop | BTC | DOWN | 0.63 | 0.80 | 1.41 |
| 10-13 09:54 | +10 | BTC | DOWN | 0.63 | 0.80 | 1.41 |
| 10-13 09:54 | +5 | BTC | DOWN | 0.63 | 0.71 | 0.48 |
| 10-13 09:52 | +10 stop | ETH | UP | 0.61 | 0.72 | 0.78 |
| 10-13 09:52 | +10 stop | BTC | UP | 0.53 | 0.29 | -2.73 |
| 10-13 09:52 | +10 stop | ZEC | UP | 0.56 | 0.40 | -1.95 |
| 10-13 09:51 | +10 stop | BNB | DOWN | 0.70 | 0.85 | 1.22 |
| 10-13 09:51 | +20 | BNB | DOWN | 0.70 | 0.92 | 1.92 |
| 10-13 09:51 | +15 | BNB | DOWN | 0.70 | 0.87 | 1.43 |
| 10-13 09:51 | +10 | BNB | DOWN | 0.70 | 0.85 | 1.22 |
| 10-13 09:51 | +5 | BNB | DOWN | 0.70 | 0.85 | 1.22 |
| 10-13 09:50 | +10 stop | BTC | DOWN | 0.59 | 0.42 | -2.05 |
| 10-13 09:50 | +20 | BTC | DOWN | 0.59 | 0.80 | 1.81 |
| 10-13 09:50 | +15 | BTC | DOWN | 0.59 | 0.80 | 1.81 |
| 10-13 09:50 | +10 | BTC | DOWN | 0.59 | 0.70 | 0.78 |
| 10-13 09:50 | +5 | BTC | DOWN | 0.59 | 0.70 | 0.78 |
| 10-13 09:50 | +10 stop | ETH | DOWN | 0.54 | 0.39 | -1.85 |
| 10-13 09:50 | +20 | ETH | DOWN | 0.54 | open |  |
| 10-13 09:50 | +15 | ETH | DOWN | 0.54 | open |  |
| 10-13 09:50 | +10 | ETH | DOWN | 0.55 | open |  |
| 10-13 09:50 | +5 | ETH | DOWN | 0.55 | open |  |
| 10-13 09:49 | +10 stop | ZEC | DOWN | 0.70 | 0.53 | -2.03 |
| 10-13 09:49 | +20 | ZEC | DOWN | 0.70 | 0.90 | 1.80 |
| 10-13 09:49 | +15 | ZEC | DOWN | 0.70 | 0.88 | 1.57 |
| 10-13 09:49 | +10 | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-13 09:49 | +5 | ZEC | DOWN | 0.70 | 0.79 | 0.63 |
| 10-13 09:38 | +10 stop | SOL | UP | 0.61 | 0.72 | 0.75 |
| 10-13 09:37 | +10 stop | ZEC | UP | 0.71 | 0.83 | 0.95 |
| 10-13 09:37 | +10 stop | HYPE | UP | 0.70 | 0.83 | 1.05 |
| 10-13 09:37 | +10 stop | DOGE | DOWN | 0.58 | 0.34 | -2.74 |
| 10-13 09:37 | +15 | DOGE | DOWN | 0.58 | yes | -5.98 |
| 10-13 09:37 | +10 | DOGE | DOWN | 0.58 | yes | -5.98 |
| 10-13 09:37 | +5 | DOGE | DOWN | 0.59 | yes | -6.07 |
| 10-13 09:36 | +10 stop | SOL | DOWN | 0.59 | 0.29 | -3.32 |
| 10-13 09:36 | +15 | SOL | DOWN | 0.59 | 0.93 | 3.18 |
| 10-13 09:36 | +10 | SOL | DOWN | 0.59 | 0.93 | 3.18 |
| 10-13 09:36 | +5 | SOL | DOWN | 0.59 | 0.93 | 3.18 |
