# Range-Scalp Bot

*Updated Mon Nov 16 02:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 61582 | 53740 | 7842 (115) | 6 | $-16551.52 | -4.3% |
| **+10¢** | 46006 | 36815 | 9191 (156) | 5 | $-15515.78 | -5.4% |
| **+15¢** | 38548 | 28633 | 9915 (195) | 6 | $-14147.10 | -5.8% |
| **+20¢** | 34362 | 23962 | 10400 (247) | 6 | $-12388.01 | -5.7% |
| **+10¢ (15¢ stop)** | 74957 | 74803 | 154 (90) | 0 | $-27554.27 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-16 02:56 | +10 stop | SOL | DOWN | 0.62 | 0.79 | 1.41 |
| 11-16 02:55 | +10 stop | ETH | DOWN | 0.63 | 0.74 | 0.79 |
| 11-16 02:55 | +10 stop | BTC | DOWN | 0.63 | 0.46 | -2.05 |
| 11-16 02:55 | +10 stop | ZEC | DOWN | 0.68 | 0.82 | 1.13 |
| 11-16 02:55 | +20 | ZEC | DOWN | 0.68 | open |  |
| 11-16 02:55 | +15 | ZEC | DOWN | 0.68 | open |  |
| 11-16 02:55 | +10 | ZEC | DOWN | 0.69 | 0.82 | 1.04 |
| 11-16 02:55 | +5 | ZEC | DOWN | 0.71 | 0.82 | 0.84 |
| 11-16 02:55 | +10 stop | XRP | DOWN | 0.61 | 0.82 | 1.82 |
| 11-16 02:55 | +20 | XRP | DOWN | 0.61 | 0.82 | 1.82 |
| 11-16 02:55 | +15 | XRP | DOWN | 0.62 | 0.82 | 1.72 |
| 11-16 02:55 | +10 | XRP | DOWN | 0.62 | 0.82 | 1.72 |
| 11-16 02:54 | +10 | DOGE | DOWN | 0.55 | open |  |
| 11-16 02:53 | +10 stop | NEAR | UP | 0.68 | 0.90 | 1.97 |
| 11-16 02:53 | +10 stop | HYPE | DOWN | 0.70 | 0.25 | -4.79 |
| 11-16 02:53 | +20 | HYPE | DOWN | 0.70 | open |  |
| 11-16 02:53 | +15 | HYPE | DOWN | 0.70 | open |  |
| 11-16 02:53 | +10 | HYPE | DOWN | 0.70 | open |  |
| 11-16 02:53 | +5 | HYPE | DOWN | 0.70 | open |  |
| 11-16 02:53 | +10 | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 11-16 02:52 | +10 stop | DOGE | DOWN | 0.70 | 0.53 | -2.03 |
| 11-16 02:52 | +20 | DOGE | DOWN | 0.70 | open |  |
| 11-16 02:52 | +15 | DOGE | DOWN | 0.71 | open |  |
| 11-16 02:52 | +10 stop | NEAR | DOWN | 0.61 | 0.38 | -2.64 |
| 11-16 02:51 | +10 stop | DOGE | DOWN | 0.66 | 0.78 | 0.91 |
| 11-16 02:51 | +10 | DOGE | DOWN | 0.66 | 0.78 | 0.91 |
| 11-16 02:50 | +10 stop | SOL | UP | 0.53 | 0.26 | -3.02 |
| 11-16 02:50 | +10 stop | ETH | DOWN | 0.53 | 0.76 | 1.99 |
| 11-16 02:50 | +5 | HYPE | DOWN | 0.60 | 0.68 | 0.47 |
| 11-16 02:49 | +10 stop | NEAR | DOWN | 0.60 | 0.70 | 0.68 |
| 11-16 02:48 | +10 stop | HYPE | DOWN | 0.62 | 0.74 | 0.90 |
| 11-16 02:48 | +10 stop | ZEC | DOWN | 0.64 | 0.88 | 2.15 |
| 11-16 02:48 | +10 stop | BTC | UP | 0.66 | 0.30 | -3.91 |
| 11-16 02:48 | +15 | BTC | UP | 0.66 | open |  |
| 11-16 02:48 | +10 | BTC | UP | 0.65 | open |  |
| 11-16 02:48 | +5 | BTC | UP | 0.65 | open |  |
| 11-16 02:48 | +5 | SOL | UP | 0.60 | open |  |
| 11-16 02:48 | +5 | ETH | UP | 0.58 | open |  |
| 11-16 02:48 | +10 stop | XRP | UP | 0.57 | 0.29 | -3.12 |
| 11-16 02:48 | +10 stop | DOGE | UP | 0.57 | 0.40 | -2.05 |
