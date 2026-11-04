# Range-Scalp Bot

*Updated Wed Nov 04 09:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 47047 | 40970 | 6077 (72) | 1 | $-13543.11 | -4.6% |
| **+10¢** | 35146 | 28097 | 7049 (97) | 1 | $-12365.55 | -5.6% |
| **+15¢** | 29434 | 21845 | 7589 (125) | 1 | $-11331.07 | -6.1% |
| **+20¢** | 26148 | 18198 | 7950 (165) | 1 | $-10002.66 | -6.1% |
| **+10¢ (15¢ stop)** | 57330 | 57237 | 93 (56) | 1 | $-21361.59 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 09:41 | +10 stop | HYPE | DOWN | 0.71 | 0.53 | -2.13 |
| 11-04 09:41 | +20 | HYPE | DOWN | 0.71 | 0.95 | 2.23 |
| 11-04 09:41 | +15 | HYPE | DOWN | 0.71 | 0.95 | 2.23 |
| 11-04 09:41 | +10 | HYPE | DOWN | 0.71 | 0.95 | 2.23 |
| 11-04 09:41 | +5 | HYPE | DOWN | 0.71 | 0.76 | 0.22 |
| 11-04 09:41 | +10 stop | SOL | UP | 0.59 | open |  |
| 11-04 09:41 | +20 | SOL | UP | 0.59 | open |  |
| 11-04 09:41 | +15 | SOL | UP | 0.59 | open |  |
| 11-04 09:41 | +10 | SOL | UP | 0.59 | open |  |
| 11-04 09:41 | +5 | SOL | UP | 0.59 | open |  |
| 11-04 09:34 | +10 stop | ZEC | UP | 0.68 | 0.78 | 0.71 |
| 11-04 09:34 | +15 | ZEC | UP | 0.68 | 0.86 | 1.55 |
| 11-04 09:34 | +10 | ZEC | UP | 0.68 | 0.78 | 0.71 |
| 11-04 09:34 | +5 | ZEC | UP | 0.68 | 0.75 | 0.40 |
| 11-04 09:34 | +10 stop | NEAR | UP | 0.68 | 0.78 | 0.71 |
| 11-04 09:34 | +20 | NEAR | UP | 0.68 | 0.90 | 1.97 |
| 11-04 09:34 | +15 | NEAR | UP | 0.68 | 0.86 | 1.55 |
| 11-04 09:34 | +10 | NEAR | UP | 0.68 | 0.78 | 0.71 |
| 11-04 09:34 | +5 | NEAR | UP | 0.67 | 0.72 | 0.19 |
| 11-04 09:31 | +10 stop | SOL | UP | 0.66 | 0.81 | 1.23 |
| 11-04 09:31 | +20 | SOL | UP | 0.66 | 0.91 | 2.31 |
| 11-04 09:31 | +15 | SOL | UP | 0.66 | 0.81 | 1.23 |
| 11-04 09:31 | +10 | SOL | UP | 0.66 | 0.81 | 1.23 |
| 11-04 09:31 | +5 | SOL | UP | 0.66 | 0.81 | 1.23 |
| 11-04 09:31 | +10 stop | ZEC | UP | 0.65 | 0.80 | 1.22 |
| 11-04 09:31 | +20 | ZEC | UP | 0.65 | 0.86 | 1.85 |
| 11-04 09:31 | +15 | ZEC | UP | 0.65 | 0.80 | 1.22 |
| 11-04 09:31 | +10 | ZEC | UP | 0.65 | 0.80 | 1.22 |
| 11-04 09:31 | +5 | ZEC | UP | 0.65 | 0.72 | 0.39 |
| 11-04 09:30 | +10 stop | HYPE | UP | 0.62 | 0.78 | 1.30 |
| 11-04 09:30 | +20 | HYPE | UP | 0.62 | 0.85 | 2.04 |
| 11-04 09:30 | +15 | HYPE | UP | 0.62 | 0.78 | 1.30 |
| 11-04 09:30 | +10 | HYPE | UP | 0.62 | 0.78 | 1.30 |
| 11-04 09:30 | +5 | HYPE | UP | 0.62 | 0.69 | 0.38 |
| 11-04 09:18 | +5 | ETH | DOWN | 0.70 | 0.75 | 0.21 |
| 11-04 09:18 | +5 | NEAR | UP | 0.57 | no | -5.88 |
| 11-04 09:18 | +5 | BTC | DOWN | 0.67 | 0.74 | 0.40 |
| 11-04 09:18 | +5 | XRP | DOWN | 0.60 | 0.67 | 0.37 |
| 11-04 09:17 | +10 stop | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 11-04 09:17 | +5 | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
