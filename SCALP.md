# Range-Scalp Bot

*Updated Sun Nov 15 06:37 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 60493 | 52769 | 7724 (107) | 1 | $-16454.60 | -4.3% |
| **+10¢** | 45196 | 36145 | 9051 (143) | 0 | $-15525.81 | -5.5% |
| **+15¢** | 37861 | 28096 | 9765 (181) | 0 | $-14218.26 | -6.0% |
| **+20¢** | 33748 | 23506 | 10242 (233) | 0 | $-12500.98 | -5.9% |
| **+10¢ (15¢ stop)** | 73640 | 73497 | 143 (82) | 0 | $-27112.44 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 06:35 | +10 | XRP | DOWN | 0.67 | 0.79 | 0.92 |
| 11-15 06:34 | +10 stop | XRP | DOWN | 0.64 | 0.75 | 0.79 |
| 11-15 06:33 | +5 | HYPE | DOWN | 0.64 | 0.70 | 0.28 |
| 11-15 06:33 | +5 | BTC | DOWN | 0.57 | 0.66 | 0.56 |
| 11-15 06:33 | +10 stop | SOL | DOWN | 0.55 | 0.69 | 1.07 |
| 11-15 06:32 | +5 | NEAR | DOWN | 0.63 | 0.73 | 0.69 |
| 11-15 06:32 | +5 | XRP | UP | 0.56 | open |  |
| 11-15 06:31 | +10 stop | HYPE | DOWN | 0.56 | 0.70 | 1.07 |
| 11-15 06:31 | +20 | HYPE | DOWN | 0.56 | 0.77 | 1.79 |
| 11-15 06:31 | +15 | HYPE | DOWN | 0.56 | 0.74 | 1.48 |
| 11-15 06:31 | +10 | HYPE | DOWN | 0.56 | 0.70 | 1.07 |
| 11-15 06:31 | +5 | HYPE | DOWN | 0.57 | 0.62 | 0.15 |
| 11-15 06:31 | +10 stop | BTC | DOWN | 0.55 | 0.66 | 0.76 |
| 11-15 06:31 | +20 | BTC | DOWN | 0.55 | 0.76 | 1.79 |
| 11-15 06:31 | +15 | BTC | DOWN | 0.55 | 0.70 | 1.17 |
| 11-15 06:31 | +10 | BTC | DOWN | 0.55 | 0.66 | 0.76 |
| 11-15 06:31 | +5 | BTC | DOWN | 0.55 | 0.60 | 0.15 |
| 11-15 06:31 | +10 stop | SOL | DOWN | 0.57 | 0.41 | -1.95 |
| 11-15 06:31 | +20 | SOL | DOWN | 0.57 | 0.80 | 2.00 |
| 11-15 06:31 | +15 | SOL | DOWN | 0.57 | 0.74 | 1.38 |
| 11-15 06:31 | +10 | SOL | DOWN | 0.57 | 0.69 | 0.87 |
| 11-15 06:31 | +5 | SOL | DOWN | 0.57 | 0.62 | 0.15 |
| 11-15 06:31 | +10 stop | ZEC | DOWN | 0.65 | 0.78 | 1.01 |
| 11-15 06:31 | +20 | ZEC | DOWN | 0.65 | 0.87 | 1.96 |
| 11-15 06:31 | +15 | ZEC | DOWN | 0.65 | 0.82 | 1.43 |
| 11-15 06:31 | +10 | ZEC | DOWN | 0.65 | 0.78 | 1.01 |
| 11-15 06:31 | +5 | ZEC | DOWN | 0.65 | 0.78 | 1.01 |
| 11-15 06:31 | +10 stop | NEAR | DOWN | 0.57 | 0.67 | 0.66 |
| 11-15 06:31 | +20 | NEAR | DOWN | 0.57 | 0.79 | 1.90 |
| 11-15 06:31 | +15 | NEAR | DOWN | 0.57 | 0.73 | 1.28 |
| 11-15 06:31 | +10 | NEAR | DOWN | 0.57 | 0.67 | 0.66 |
| 11-15 06:31 | +5 | NEAR | DOWN | 0.57 | 0.66 | 0.56 |
| 11-15 06:31 | +10 stop | BNB | DOWN | 0.56 | 0.67 | 0.76 |
| 11-15 06:31 | +20 | BNB | DOWN | 0.56 | 0.76 | 1.69 |
| 11-15 06:31 | +15 | BNB | DOWN | 0.56 | 0.74 | 1.48 |
| 11-15 06:31 | +10 | BNB | DOWN | 0.57 | 0.67 | 0.66 |
| 11-15 06:31 | +5 | BNB | DOWN | 0.57 | 0.67 | 0.66 |
| 11-15 06:31 | +10 stop | XRP | DOWN | 0.50 | 0.60 | 0.65 |
| 11-15 06:31 | +20 | XRP | DOWN | 0.50 | 0.72 | 1.87 |
| 11-15 06:31 | +15 | XRP | DOWN | 0.50 | 0.66 | 1.26 |
