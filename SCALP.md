# Range-Scalp Bot

*Updated Thu Oct 29 01:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 38771 | 33837 | 4934 (49) | 5 | $-10861.30 | -4.4% |
| **+10¢** | 28918 | 23220 | 5698 (71) | 6 | $-9621.55 | -5.3% |
| **+15¢** | 24190 | 18068 | 6122 (97) | 6 | $-8572.21 | -5.6% |
| **+20¢** | 21458 | 15047 | 6411 (125) | 8 | $-7475.69 | -5.5% |
| **+10¢ (15¢ stop)** | 47414 | 47347 | 67 (35) | 0 | $-17981.61 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-29 01:25 | +10 stop | XRP | DOWN | 0.44 | 0.62 | 1.45 |
| 10-29 01:25 | +15 | XRP | DOWN | 0.44 | 0.62 | 1.45 |
| 10-29 01:25 | +5 | XRP | DOWN | 0.45 | 0.62 | 1.35 |
| 10-29 01:25 | +10 stop | SOL | DOWN | 0.70 | 0.54 | -1.93 |
| 10-29 01:19 | +10 stop | XRP | DOWN | 0.64 | 0.77 | 1.00 |
| 10-29 01:19 | +15 | XRP | DOWN | 0.64 | 0.83 | 1.63 |
| 10-29 01:19 | +5 | XRP | DOWN | 0.64 | 0.73 | 0.59 |
| 10-29 01:19 | +10 stop | HYPE | DOWN | 0.66 | 0.78 | 0.91 |
| 10-29 01:19 | +15 | HYPE | DOWN | 0.67 | 0.83 | 1.30 |
| 10-29 01:19 | +10 | HYPE | DOWN | 0.67 | 0.78 | 0.77 |
| 10-29 01:19 | +5 | HYPE | DOWN | 0.67 | 0.78 | 0.77 |
| 10-29 01:19 | +10 stop | NEAR | DOWN | 0.68 | 0.80 | 0.92 |
| 10-29 01:19 | +10 | NEAR | DOWN | 0.68 | 0.80 | 0.92 |
| 10-29 01:19 | +5 | NEAR | DOWN | 0.68 | 0.74 | 0.30 |
| 10-29 01:19 | +10 stop | BTC | DOWN | 0.67 | 0.78 | 0.81 |
| 10-29 01:19 | +10 stop | ETH | DOWN | 0.71 | 0.83 | 0.95 |
| 10-29 01:19 | +10 | ETH | DOWN | 0.71 | 0.83 | 0.95 |
| 10-29 01:19 | +5 | ETH | DOWN | 0.71 | 0.80 | 0.63 |
| 10-29 01:19 | +10 stop | SOL | DOWN | 0.68 | 0.78 | 0.71 |
| 10-29 01:18 | +10 stop | NEAR | UP | 0.48 | 0.60 | 0.85 |
| 10-29 01:18 | +10 | NEAR | UP | 0.48 | 0.60 | 0.85 |
| 10-29 01:18 | +5 | NEAR | UP | 0.48 | 0.60 | 0.85 |
| 10-29 01:18 | +10 stop | ETH | UP | 0.53 | 0.66 | 0.96 |
| 10-29 01:18 | +5 | SOL | UP | 0.53 | open |  |
| 10-29 01:17 | +10 stop | XRP | UP | 0.65 | 0.50 | -1.86 |
| 10-29 01:17 | +10 | XRP | UP | 0.65 | open |  |
| 10-29 01:17 | +5 | ZEC | UP | 0.62 | open |  |
| 10-29 01:17 | +5 | XRP | UP | 0.65 | 0.74 | 0.60 |
| 10-29 01:17 | +10 stop | SOL | UP | 0.58 | 0.37 | -2.45 |
| 10-29 01:17 | +20 | SOL | UP | 0.58 | open |  |
| 10-29 01:17 | +15 | SOL | UP | 0.58 | open |  |
| 10-29 01:17 | +10 | SOL | UP | 0.58 | open |  |
| 10-29 01:17 | +5 | SOL | UP | 0.58 | 0.64 | 0.25 |
| 10-29 01:16 | +10 stop | HYPE | UP | 0.59 | 0.70 | 0.78 |
| 10-29 01:16 | +20 | HYPE | UP | 0.59 | open |  |
| 10-29 01:16 | +15 | HYPE | UP | 0.59 | 0.75 | 1.29 |
| 10-29 01:16 | +10 | HYPE | UP | 0.59 | 0.70 | 0.78 |
| 10-29 01:16 | +5 | HYPE | UP | 0.59 | 0.70 | 0.78 |
| 10-29 01:16 | +10 stop | BTC | UP | 0.59 | 0.43 | -1.95 |
| 10-29 01:16 | +20 | BTC | UP | 0.59 | open |  |
