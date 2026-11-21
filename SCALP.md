# Range-Scalp Bot

*Updated Sat Nov 21 23:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 67926 | 59291 | 8635 (138) | 3 | $-18140.53 | -4.2% |
| **+10¢** | 50716 | 40626 | 10090 (181) | 3 | $-16823.83 | -5.3% |
| **+15¢** | 42516 | 31638 | 10878 (230) | 3 | $-15081.56 | -5.7% |
| **+20¢** | 37846 | 26412 | 11434 (288) | 3 | $-13412.73 | -5.7% |
| **+10¢ (15¢ stop)** | 82691 | 82513 | 178 (110) | 1 | $-30370.77 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-21 23:26 | +10 stop | DOGE | DOWN | 0.66 | open |  |
| 11-21 23:26 | +5 | DOGE | DOWN | 0.66 | open |  |
| 11-21 23:25 | +5 | NEAR | UP | 0.61 | 0.71 | 0.68 |
| 11-21 23:25 | +10 stop | NEAR | UP | 0.61 | 0.71 | 0.71 |
| 11-21 23:25 | +10 stop | HYPE | UP | 0.68 | 0.88 | 1.76 |
| 11-21 23:25 | +20 | HYPE | UP | 0.68 | 0.88 | 1.76 |
| 11-21 23:25 | +15 | HYPE | UP | 0.68 | 0.88 | 1.76 |
| 11-21 23:25 | +10 | HYPE | UP | 0.68 | 0.88 | 1.76 |
| 11-21 23:25 | +5 | HYPE | UP | 0.68 | 0.88 | 1.76 |
| 11-21 23:24 | +10 stop | NEAR | UP | 0.58 | 0.38 | -2.35 |
| 11-21 23:24 | +20 | NEAR | UP | 0.58 | 0.87 | 2.64 |
| 11-21 23:24 | +15 | NEAR | UP | 0.58 | 0.87 | 2.64 |
| 11-21 23:24 | +10 | NEAR | UP | 0.58 | 0.71 | 0.97 |
| 11-21 23:24 | +5 | NEAR | UP | 0.58 | 0.64 | 0.25 |
| 11-21 23:22 | +10 stop | DOGE | UP | 0.63 | 0.18 | -4.78 |
| 11-21 23:22 | +10 | DOGE | UP | 0.63 | open |  |
| 11-21 23:22 | +5 | DOGE | UP | 0.62 | 0.67 | 0.17 |
| 11-21 23:22 | +10 stop | ZEC | DOWN | 0.63 | 0.73 | 0.69 |
| 11-21 23:20 | +10 stop | ZEC | UP | 0.63 | 0.43 | -2.35 |
| 11-21 23:20 | +5 | ZEC | UP | 0.63 | open |  |
| 11-21 23:20 | +5 | ETH | UP | 0.64 | open |  |
| 11-21 23:20 | +10 stop | BTC | UP | 0.54 | 0.21 | -3.60 |
| 11-21 23:20 | +10 stop | DOGE | UP | 0.60 | 0.72 | 0.88 |
| 11-21 23:20 | +10 stop | SOL | UP | 0.60 | 0.71 | 0.78 |
| 11-21 23:20 | +10 stop | ETH | UP | 0.69 | 0.23 | -4.88 |
| 11-21 23:19 | +10 stop | BTC | DOWN | 0.61 | 0.37 | -2.74 |
| 11-21 23:19 | +10 | BTC | DOWN | 0.61 | 0.78 | 1.40 |
| 11-21 23:19 | +5 | BTC | DOWN | 0.61 | 0.78 | 1.40 |
| 11-21 23:19 | +10 stop | ZEC | DOWN | 0.56 | 0.36 | -2.35 |
| 11-21 23:19 | +10 stop | SOL | DOWN | 0.59 | 0.44 | -1.85 |
| 11-21 23:19 | +20 | SOL | DOWN | 0.59 | 0.85 | 2.34 |
| 11-21 23:19 | +15 | SOL | DOWN | 0.59 | 0.76 | 1.40 |
| 11-21 23:19 | +10 | SOL | DOWN | 0.59 | 0.76 | 1.40 |
| 11-21 23:19 | +5 | SOL | DOWN | 0.59 | 0.76 | 1.40 |
| 11-21 23:19 | +5 | HYPE | UP | 0.62 | 0.69 | 0.38 |
| 11-21 23:18 | +10 stop | DOGE | DOWN | 0.69 | 0.45 | -2.73 |
| 11-21 23:18 | +5 | BTC | DOWN | 0.62 | 0.72 | 0.68 |
| 11-21 23:18 | +5 | ZEC | UP | 0.65 | 0.72 | 0.39 |
| 11-21 23:18 | +10 stop | ZEC | UP | 0.63 | 0.39 | -2.74 |
| 11-21 23:18 | +10 | ZEC | UP | 0.63 | open |  |
