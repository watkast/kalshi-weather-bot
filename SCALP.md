# Range-Scalp Bot

*Updated Mon Nov 09 11:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 53606 | 46751 | 6855 (86) | 1 | $-14705.45 | -4.4% |
| **+10¢** | 40047 | 32051 | 7996 (112) | 2 | $-13684.11 | -5.4% |
| **+15¢** | 33556 | 24939 | 8617 (143) | 2 | $-12484.73 | -5.9% |
| **+20¢** | 29860 | 20821 | 9039 (189) | 3 | $-10978.40 | -5.9% |
| **+10¢ (15¢ stop)** | 65333 | 65227 | 106 (63) | 0 | $-24196.46 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-09 11:42 | +10 stop | XRP | DOWN | 0.34 | 0.53 | 1.56 |
| 11-09 11:42 | +20 | XRP | DOWN | 0.35 | open |  |
| 11-09 11:42 | +15 | XRP | DOWN | 0.33 | 0.53 | 1.66 |
| 11-09 11:42 | +10 | XRP | DOWN | 0.33 | 0.53 | 1.66 |
| 11-09 11:42 | +5 | XRP | DOWN | 0.33 | 0.53 | 1.66 |
| 11-09 11:42 | +10 stop | XRP | UP | 0.45 | 0.66 | 1.76 |
| 11-09 11:42 | +20 | XRP | UP | 0.45 | 0.66 | 1.76 |
| 11-09 11:42 | +15 | XRP | UP | 0.45 | 0.66 | 1.76 |
| 11-09 11:42 | +10 | XRP | UP | 0.46 | 0.66 | 1.66 |
| 11-09 11:42 | +5 | XRP | UP | 0.50 | 0.66 | 1.26 |
| 11-09 11:41 | +10 stop | HYPE | DOWN | 0.63 | 0.79 | 1.31 |
| 11-09 11:40 | +10 stop | HYPE | UP | 0.42 | 0.56 | 1.04 |
| 11-09 11:40 | +10 stop | ZEC | UP | 0.51 | 0.33 | -2.14 |
| 11-09 11:38 | +10 | HYPE | DOWN | 0.71 | 0.90 | 1.68 |
| 11-09 11:38 | +10 stop | ZEC | DOWN | 0.70 | 0.49 | -2.43 |
| 11-09 11:37 | +10 stop | DOGE | UP | 0.55 | 0.74 | 1.58 |
| 11-09 11:37 | +15 | DOGE | UP | 0.55 | 0.74 | 1.58 |
| 11-09 11:37 | +10 | DOGE | UP | 0.55 | 0.74 | 1.58 |
| 11-09 11:37 | +5 | DOGE | UP | 0.55 | 0.64 | 0.55 |
| 11-09 11:37 | +10 stop | XRP | UP | 0.55 | 0.68 | 0.96 |
| 11-09 11:37 | +10 stop | SOL | DOWN | 0.69 | 0.81 | 0.94 |
| 11-09 11:37 | +5 | HYPE | DOWN | 0.69 | 0.79 | 0.73 |
| 11-09 11:36 | +10 stop | NEAR | DOWN | 0.58 | 0.41 | -2.05 |
| 11-09 11:36 | +10 | NEAR | DOWN | 0.57 | 0.74 | 1.38 |
| 11-09 11:36 | +10 stop | HYPE | DOWN | 0.67 | 0.48 | -2.19 |
| 11-09 11:36 | +10 stop | ZEC | DOWN | 0.68 | 0.50 | -2.14 |
| 11-09 11:35 | +10 stop | NEAR | UP | 0.64 | 0.47 | -2.05 |
| 11-09 11:35 | +10 stop | XRP | UP | 0.63 | 0.48 | -1.85 |
| 11-09 11:35 | +10 stop | ZEC | UP | 0.60 | 0.40 | -2.33 |
| 11-09 11:35 | +10 stop | SOL | UP | 0.57 | 0.40 | -2.05 |
| 11-09 11:35 | +10 | SOL | UP | 0.59 | open |  |
| 11-09 11:35 | +10 stop | HYPE | UP | 0.71 | 0.55 | -1.93 |
| 11-09 11:34 | +5 | BTC | UP | 0.71 | 0.82 | 0.84 |
| 11-09 11:34 | +10 stop | NEAR | DOWN | 0.59 | 0.35 | -2.73 |
| 11-09 11:34 | +5 | NEAR | DOWN | 0.59 | 0.74 | 1.19 |
| 11-09 11:33 | +10 stop | SOL | DOWN | 0.71 | 0.39 | -3.52 |
| 11-09 11:33 | +5 | SOL | DOWN | 0.71 | 0.76 | 0.22 |
| 11-09 11:33 | +10 stop | NEAR | DOWN | 0.46 | 0.59 | 0.95 |
| 11-09 11:33 | +10 stop | DOGE | DOWN | 0.54 | 0.33 | -2.44 |
| 11-09 11:33 | +10 stop | ZEC | DOWN | 0.51 | 0.32 | -2.24 |
