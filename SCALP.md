# Range-Scalp Bot

*Updated Sun Nov 15 22:23 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 61298 | 53488 | 7810 (114) | 5 | $-16499.85 | -4.3% |
| **+10¢** | 45780 | 36629 | 9151 (153) | 6 | $-15496.08 | -5.4% |
| **+15¢** | 38345 | 28474 | 9871 (191) | 7 | $-14152.94 | -5.9% |
| **+20¢** | 34178 | 23822 | 10356 (243) | 7 | $-12436.31 | -5.8% |
| **+10¢ (15¢ stop)** | 74590 | 74438 | 152 (90) | 3 | $-27431.89 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 22:22 | +10 stop | HYPE | DOWN | 0.59 | open |  |
| 11-15 22:22 | +10 | HYPE | DOWN | 0.59 | open |  |
| 11-15 22:22 | +5 | HYPE | DOWN | 0.59 | open |  |
| 11-15 22:22 | +10 stop | BNB | UP | 0.70 | open |  |
| 11-15 22:22 | +20 | BNB | UP | 0.70 | open |  |
| 11-15 22:22 | +15 | BNB | UP | 0.70 | open |  |
| 11-15 22:22 | +10 | BNB | UP | 0.70 | open |  |
| 11-15 22:22 | +5 | BNB | UP | 0.70 | 0.75 | 0.21 |
| 11-15 22:22 | +10 stop | SOL | UP | 0.58 | open |  |
| 11-15 22:22 | +15 | SOL | UP | 0.58 | open |  |
| 11-15 22:22 | +10 | SOL | UP | 0.58 | open |  |
| 11-15 22:22 | +5 | SOL | UP | 0.58 | open |  |
| 11-15 22:22 | +10 stop | XRP | UP | 0.62 | 0.73 | 0.79 |
| 11-15 22:22 | +15 | XRP | UP | 0.62 | open |  |
| 11-15 22:22 | +10 | XRP | UP | 0.62 | 0.73 | 0.79 |
| 11-15 22:22 | +5 | XRP | UP | 0.62 | 0.73 | 0.79 |
| 11-15 22:21 | +10 | HYPE | UP | 0.51 | 0.61 | 0.65 |
| 11-15 22:21 | +5 | HYPE | UP | 0.51 | 0.61 | 0.65 |
| 11-15 22:20 | +5 | ZEC | UP | 0.67 | open |  |
| 11-15 22:20 | +10 stop | BTC | UP | 0.61 | 0.46 | -1.85 |
| 11-15 22:20 | +5 | BTC | UP | 0.61 | open |  |
| 11-15 22:20 | +10 stop | HYPE | UP | 0.68 | 0.50 | -2.13 |
| 11-15 22:18 | +10 stop | SOL | UP | 0.63 | 0.77 | 1.10 |
| 11-15 22:18 | +10 | SOL | UP | 0.63 | 0.77 | 1.10 |
| 11-15 22:18 | +5 | SOL | UP | 0.63 | 0.70 | 0.38 |
| 11-15 22:17 | +10 stop | ZEC | UP | 0.65 | 0.46 | -2.24 |
| 11-15 22:17 | +15 | ZEC | UP | 0.68 | open |  |
| 11-15 22:17 | +10 | ZEC | UP | 0.68 | open |  |
| 11-15 22:17 | +5 | ZEC | UP | 0.68 | 0.74 | 0.30 |
| 11-15 22:17 | +5 | BTC | UP | 0.66 | 0.72 | 0.29 |
| 11-15 22:17 | +10 stop | XRP | UP | 0.66 | 0.76 | 0.71 |
| 11-15 22:17 | +20 | XRP | UP | 0.65 | open |  |
| 11-15 22:17 | +15 | XRP | UP | 0.65 | 0.81 | 1.32 |
| 11-15 22:17 | +10 | XRP | UP | 0.65 | 0.76 | 0.81 |
| 11-15 22:17 | +5 | XRP | UP | 0.65 | 0.74 | 0.60 |
| 11-15 22:17 | +10 stop | HYPE | UP | 0.64 | 0.49 | -1.85 |
| 11-15 22:17 | +20 | HYPE | UP | 0.65 | open |  |
| 11-15 22:17 | +15 | HYPE | UP | 0.65 | open |  |
| 11-15 22:17 | +10 | HYPE | UP | 0.65 | 0.77 | 0.91 |
| 11-15 22:17 | +5 | HYPE | UP | 0.65 | 0.70 | 0.19 |
