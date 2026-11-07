# Range-Scalp Bot

*Updated Sat Nov 07 21:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 51502 | 44909 | 6593 (80) | 1 | $-14267.51 | -4.4% |
| **+10¢** | 38433 | 30745 | 7688 (106) | 1 | $-13280.18 | -5.5% |
| **+15¢** | 32180 | 23895 | 8285 (135) | 1 | $-12174.64 | -6.0% |
| **+20¢** | 28625 | 19941 | 8684 (178) | 1 | $-10724.65 | -6.0% |
| **+10¢ (15¢ stop)** | 62708 | 62605 | 103 (61) | 1 | $-23190.92 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 21:01 | +15 | ZEC | UP | 0.70 | open |  |
| 11-07 21:01 | +10 | ZEC | UP | 0.70 | open |  |
| 11-07 21:01 | +5 | ZEC | UP | 0.69 | open |  |
| 11-07 21:01 | +10 stop | ZEC | UP | 0.70 | open |  |
| 11-07 21:01 | +20 | ZEC | UP | 0.70 | open |  |
| 11-07 21:00 | +10 stop | DOGE | UP | 0.56 | 0.75 | 1.58 |
| 11-07 21:00 | +20 | DOGE | UP | 0.56 | 0.77 | 1.79 |
| 11-07 21:00 | +15 | DOGE | UP | 0.54 | 0.75 | 1.78 |
| 11-07 21:00 | +10 | DOGE | UP | 0.54 | 0.64 | 0.65 |
| 11-07 21:00 | +5 | DOGE | UP | 0.54 | 0.64 | 0.65 |
| 11-07 20:47 | +10 stop | ZEC | DOWN | 0.71 | 0.55 | -1.93 |
| 11-07 20:47 | +20 | ZEC | DOWN | 0.71 | 0.92 | 1.90 |
| 11-07 20:47 | +15 | ZEC | DOWN | 0.71 | 0.88 | 1.47 |
| 11-07 20:47 | +10 | ZEC | DOWN | 0.70 | 0.88 | 1.57 |
| 11-07 20:47 | +5 | ZEC | DOWN | 0.70 | 0.75 | 0.21 |
| 11-07 20:46 | +10 stop | HYPE | DOWN | 0.66 | 0.79 | 1.02 |
| 11-07 20:46 | +20 | HYPE | DOWN | 0.66 | 0.88 | 1.96 |
| 11-07 20:46 | +15 | HYPE | DOWN | 0.66 | 0.83 | 1.44 |
| 11-07 20:46 | +10 | HYPE | DOWN | 0.66 | 0.79 | 1.02 |
| 11-07 20:46 | +5 | HYPE | DOWN | 0.66 | 0.79 | 1.02 |
| 11-07 20:46 | +10 stop | BTC | DOWN | 0.67 | 0.81 | 1.13 |
| 11-07 20:46 | +20 | BTC | DOWN | 0.67 | 0.87 | 1.76 |
| 11-07 20:46 | +15 | BTC | DOWN | 0.67 | 0.82 | 1.23 |
| 11-07 20:46 | +10 | BTC | DOWN | 0.67 | 0.81 | 1.13 |
| 11-07 20:46 | +5 | BTC | DOWN | 0.67 | 0.73 | 0.30 |
| 11-07 20:42 | +10 stop | NEAR | UP | 0.66 | 0.35 | -3.42 |
| 11-07 20:42 | +20 | NEAR | UP | 0.66 | no | -6.76 |
| 11-07 20:42 | +15 | NEAR | UP | 0.66 | no | -6.76 |
| 11-07 20:42 | +10 | NEAR | UP | 0.66 | no | -6.76 |
| 11-07 20:42 | +5 | NEAR | UP | 0.66 | 0.72 | 0.29 |
| 11-07 20:41 | +10 stop | ZEC | UP | 0.54 | 0.38 | -1.95 |
| 11-07 20:40 | +10 stop | HYPE | DOWN | 0.71 | 0.53 | -2.13 |
| 11-07 20:40 | +5 | HYPE | DOWN | 0.70 | 0.83 | 1.05 |
| 11-07 20:40 | +10 stop | ETH | UP | 0.69 | 0.47 | -2.53 |
| 11-07 20:39 | +10 stop | ETH | DOWN | 0.62 | 0.35 | -3.03 |
| 11-07 20:39 | +10 | ETH | DOWN | 0.62 | 0.89 | 2.46 |
| 11-07 20:39 | +10 stop | ZEC | DOWN | 0.60 | 0.42 | -2.15 |
| 11-07 20:39 | +10 stop | HYPE | DOWN | 0.68 | 0.27 | -4.40 |
| 11-07 20:38 | +10 stop | ZEC | DOWN | 0.65 | 0.50 | -1.84 |
| 11-07 20:38 | +15 | ZEC | DOWN | 0.65 | 0.88 | 2.06 |
