# Range-Scalp Bot

*Updated Thu Oct 29 01:36 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 38778 | 33840 | 4938 (49) | 0 | $-10880.70 | -4.5% |
| **+10¢** | 28925 | 23222 | 5703 (71) | 0 | $-9648.41 | -5.3% |
| **+15¢** | 24198 | 18071 | 6127 (97) | 0 | $-8597.19 | -5.7% |
| **+20¢** | 21467 | 15049 | 6418 (125) | 0 | $-7513.43 | -5.6% |
| **+10¢ (15¢ stop)** | 47417 | 47350 | 67 (35) | 0 | $-17978.10 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-29 01:31 | +10 stop | BNB | DOWN | 0.70 | 0.85 | 1.26 |
| 10-29 01:31 | +20 | BNB | DOWN | 0.70 | 0.91 | 1.92 |
| 10-29 01:31 | +15 | BNB | DOWN | 0.70 | 0.85 | 1.26 |
| 10-29 01:31 | +10 | BNB | DOWN | 0.70 | 0.85 | 1.26 |
| 10-29 01:31 | +5 | BNB | DOWN | 0.70 | 0.85 | 1.22 |
| 10-29 01:26 | +10 stop | XRP | DOWN | 0.69 | 0.87 | 1.57 |
| 10-29 01:26 | +15 | XRP | DOWN | 0.69 | 0.87 | 1.57 |
| 10-29 01:26 | +5 | XRP | DOWN | 0.70 | 0.77 | 0.42 |
| 10-29 01:26 | +10 stop | BNB | DOWN | 0.60 | 0.70 | 0.68 |
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
| 10-29 01:18 | +5 | SOL | UP | 0.53 | no | -5.48 |
| 10-29 01:17 | +10 stop | XRP | UP | 0.65 | 0.50 | -1.86 |
| 10-29 01:17 | +10 | XRP | UP | 0.65 | no | -6.68 |
| 10-29 01:17 | +5 | ZEC | UP | 0.62 | no | -6.37 |
| 10-29 01:17 | +5 | XRP | UP | 0.65 | 0.74 | 0.60 |
| 10-29 01:17 | +10 stop | SOL | UP | 0.58 | 0.37 | -2.45 |
| 10-29 01:17 | +20 | SOL | UP | 0.58 | no | -5.98 |
| 10-29 01:17 | +15 | SOL | UP | 0.58 | no | -5.98 |
