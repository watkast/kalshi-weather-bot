# Range-Scalp Bot

*Updated Sat Nov 14 15:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 59499 | 51916 | 7583 (107) | 2 | $-16072.36 | -4.3% |
| **+10¢** | 44438 | 35561 | 8877 (142) | 4 | $-15098.39 | -5.4% |
| **+15¢** | 37240 | 27666 | 9574 (178) | 4 | $-13744.84 | -5.9% |
| **+20¢** | 33171 | 23123 | 10048 (230) | 5 | $-12122.28 | -5.8% |
| **+10¢ (15¢ stop)** | 72392 | 72249 | 143 (82) | 0 | $-26640.05 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 15:40 | +5 | BNB | DOWN | 0.49 | 0.61 | 0.86 |
| 11-14 15:40 | +10 stop | DOGE | DOWN | 0.38 | 0.54 | 1.25 |
| 11-14 15:40 | +10 | DOGE | DOWN | 0.38 | 0.54 | 1.25 |
| 11-14 15:40 | +5 | DOGE | DOWN | 0.38 | 0.54 | 1.25 |
| 11-14 15:40 | +10 stop | BNB | DOWN | 0.51 | 0.61 | 0.65 |
| 11-14 15:40 | +10 stop | BTC | UP | 0.66 | 0.81 | 1.23 |
| 11-14 15:39 | +10 stop | BTC | UP | 0.48 | 0.60 | 0.85 |
| 11-14 15:39 | +10 stop | SOL | DOWN | 0.70 | 0.39 | -3.42 |
| 11-14 15:38 | +10 stop | BNB | UP | 0.51 | 0.62 | 0.75 |
| 11-14 15:38 | +10 stop | ETH | UP | 0.59 | 0.25 | -3.71 |
| 11-14 15:38 | +10 stop | NEAR | DOWN | 0.69 | 0.81 | 0.94 |
| 11-14 15:38 | +10 | NEAR | DOWN | 0.70 | 0.81 | 0.84 |
| 11-14 15:38 | +5 | NEAR | DOWN | 0.70 | 0.81 | 0.84 |
| 11-14 15:38 | +10 stop | SOL | UP | 0.60 | 0.39 | -2.44 |
| 11-14 15:37 | +10 stop | HYPE | UP | 0.60 | 0.31 | -3.22 |
| 11-14 15:37 | +10 stop | XRP | UP | 0.53 | 0.35 | -2.14 |
| 11-14 15:36 | +10 stop | ZEC | DOWN | 0.66 | 0.77 | 0.85 |
| 11-14 15:36 | +20 | ZEC | DOWN | 0.66 | 0.88 | 1.96 |
| 11-14 15:36 | +15 | ZEC | DOWN | 0.66 | 0.83 | 1.44 |
| 11-14 15:36 | +10 | ZEC | DOWN | 0.65 | 0.77 | 0.91 |
| 11-14 15:36 | +5 | ZEC | DOWN | 0.66 | 0.74 | 0.50 |
| 11-14 15:36 | +10 stop | NEAR | DOWN | 0.46 | 0.58 | 0.84 |
| 11-14 15:36 | +20 | NEAR | DOWN | 0.46 | 0.67 | 1.76 |
| 11-14 15:36 | +15 | NEAR | DOWN | 0.46 | 0.64 | 1.45 |
| 11-14 15:36 | +10 | NEAR | DOWN | 0.46 | 0.58 | 0.84 |
| 11-14 15:36 | +5 | NEAR | DOWN | 0.46 | 0.58 | 0.84 |
| 11-14 15:34 | +10 stop | SOL | UP | 0.61 | 0.72 | 0.78 |
| 11-14 15:34 | +10 stop | BNB | UP | 0.66 | 0.77 | 0.81 |
| 11-14 15:34 | +10 stop | BTC | UP | 0.67 | 0.77 | 0.71 |
| 11-14 15:34 | +10 stop | ETH | UP | 0.58 | 0.69 | 0.77 |
| 11-14 15:34 | +10 stop | DOGE | UP | 0.66 | 0.78 | 0.91 |
| 11-14 15:34 | +10 | DOGE | UP | 0.66 | 0.78 | 0.91 |
| 11-14 15:34 | +5 | DOGE | UP | 0.66 | 0.78 | 0.91 |
| 11-14 15:34 | +10 stop | HYPE | DOWN | 0.61 | 0.37 | -2.74 |
| 11-14 15:34 | +10 | HYPE | DOWN | 0.61 | 0.81 | 1.72 |
| 11-14 15:34 | +5 | HYPE | DOWN | 0.63 | 0.81 | 1.52 |
| 11-14 15:33 | +10 stop | SOL | DOWN | 0.50 | 0.34 | -1.94 |
| 11-14 15:33 | +5 | XRP | DOWN | 0.71 | 0.76 | 0.22 |
| 11-14 15:33 | +15 | ETH | DOWN | 0.62 | open |  |
| 11-14 15:32 | +10 stop | BNB | DOWN | 0.58 | 0.38 | -2.35 |
