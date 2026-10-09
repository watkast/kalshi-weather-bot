# Range-Scalp Bot

*Updated Fri Oct 09 18:36 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 9329 | 8047 | 1282 (17) | 0 | $-3192.53 | -5.4% |
| **+10¢** | 7045 | 5544 | 1501 (29) | 0 | $-3104.07 | -7.0% |
| **+15¢** | 5938 | 4358 | 1580 (42) | 0 | $-2567.18 | -6.9% |
| **+20¢** | 5287 | 3646 | 1641 (53) | 0 | $-2147.84 | -6.5% |
| **+10¢ (15¢ stop)** | 11419 | 11387 | 32 (20) | 0 | $-4393.01 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-09 18:34 | +5 | XRP | DOWN | 0.65 | 0.74 | 0.60 |
| 10-09 18:34 | +5 | BNB | DOWN | 0.69 | 0.79 | 0.74 |
| 10-09 18:33 | +10 stop | SOL | DOWN | 0.69 | 0.81 | 0.94 |
| 10-09 18:33 | +10 | SOL | DOWN | 0.69 | 0.81 | 0.94 |
| 10-09 18:33 | +5 | SOL | DOWN | 0.69 | 0.74 | 0.21 |
| 10-09 18:33 | +10 stop | BTC | DOWN | 0.68 | 0.79 | 0.82 |
| 10-09 18:33 | +20 | BTC | DOWN | 0.68 | 0.88 | 1.76 |
| 10-09 18:33 | +15 | BTC | DOWN | 0.68 | 0.87 | 1.66 |
| 10-09 18:33 | +10 | BTC | DOWN | 0.68 | 0.79 | 0.82 |
| 10-09 18:33 | +5 | BTC | DOWN | 0.68 | 0.74 | 0.30 |
| 10-09 18:33 | +10 stop | ZEC | DOWN | 0.61 | 0.73 | 0.89 |
| 10-09 18:33 | +20 | ZEC | DOWN | 0.61 | 0.81 | 1.72 |
| 10-09 18:33 | +15 | ZEC | DOWN | 0.61 | 0.81 | 1.72 |
| 10-09 18:33 | +10 | ZEC | DOWN | 0.61 | 0.73 | 0.89 |
| 10-09 18:33 | +5 | ZEC | DOWN | 0.61 | 0.69 | 0.48 |
| 10-09 18:33 | +10 stop | XRP | DOWN | 0.59 | 0.74 | 1.19 |
| 10-09 18:33 | +20 | XRP | DOWN | 0.59 | 0.79 | 1.71 |
| 10-09 18:33 | +15 | XRP | DOWN | 0.59 | 0.74 | 1.19 |
| 10-09 18:33 | +10 | XRP | DOWN | 0.59 | 0.74 | 1.19 |
| 10-09 18:33 | +5 | XRP | DOWN | 0.59 | 0.67 | 0.47 |
| 10-09 18:32 | +5 | HYPE | DOWN | 0.69 | 0.75 | 0.27 |
| 10-09 18:32 | +10 stop | ETH | DOWN | 0.64 | 0.77 | 1.00 |
| 10-09 18:32 | +20 | ETH | DOWN | 0.64 | 0.84 | 1.73 |
| 10-09 18:32 | +15 | ETH | DOWN | 0.64 | 0.84 | 1.73 |
| 10-09 18:32 | +10 | ETH | DOWN | 0.64 | 0.77 | 1.00 |
| 10-09 18:32 | +5 | ETH | DOWN | 0.64 | 0.71 | 0.38 |
| 10-09 18:31 | +10 stop | NEAR | DOWN | 0.56 | 0.74 | 1.48 |
| 10-09 18:31 | +20 | NEAR | DOWN | 0.56 | 0.77 | 1.79 |
| 10-09 18:31 | +15 | NEAR | DOWN | 0.56 | 0.74 | 1.48 |
| 10-09 18:31 | +10 | NEAR | DOWN | 0.56 | 0.74 | 1.48 |
| 10-09 18:31 | +5 | NEAR | DOWN | 0.56 | 0.62 | 0.25 |
| 10-09 18:31 | +10 stop | BNB | DOWN | 0.64 | 0.79 | 1.21 |
| 10-09 18:31 | +20 | BNB | DOWN | 0.64 | 0.85 | 1.84 |
| 10-09 18:31 | +15 | BNB | DOWN | 0.64 | 0.79 | 1.21 |
| 10-09 18:31 | +10 | BNB | DOWN | 0.64 | 0.79 | 1.21 |
| 10-09 18:31 | +5 | BNB | DOWN | 0.64 | 0.69 | 0.18 |
| 10-09 18:31 | +10 stop | HYPE | DOWN | 0.59 | 0.69 | 0.68 |
| 10-09 18:31 | +20 | HYPE | DOWN | 0.59 | 0.79 | 1.71 |
| 10-09 18:31 | +15 | HYPE | DOWN | 0.59 | 0.74 | 1.19 |
| 10-09 18:31 | +10 | HYPE | DOWN | 0.59 | 0.69 | 0.68 |
