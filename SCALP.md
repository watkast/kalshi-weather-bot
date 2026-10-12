# Range-Scalp Bot

*Updated Mon Oct 12 06:08 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 13156 | 11366 | 1790 (25) | 1 | $-4302.94 | -5.2% |
| **+10¢** | 9972 | 7901 | 2071 (37) | 1 | $-4009.39 | -6.4% |
| **+15¢** | 8385 | 6171 | 2214 (55) | 1 | $-3539.34 | -6.7% |
| **+20¢** | 7465 | 5157 | 2308 (70) | 3 | $-3017.98 | -6.4% |
| **+10¢ (15¢ stop)** | 16208 | 16167 | 41 (25) | 0 | $-6372.42 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-12 06:07 | +5 | NEAR | UP | 0.64 | 0.72 | 0.48 |
| 10-12 06:07 | +20 | HYPE | DOWN | 0.70 | open |  |
| 10-12 06:06 | +10 stop | ZEC | DOWN | 0.66 | 0.50 | -1.94 |
| 10-12 06:06 | +10 stop | NEAR | UP | 0.56 | 0.72 | 1.27 |
| 10-12 06:06 | +10 | NEAR | UP | 0.56 | 0.72 | 1.27 |
| 10-12 06:06 | +5 | NEAR | UP | 0.58 | 0.65 | 0.36 |
| 10-12 06:05 | +10 stop | HYPE | DOWN | 0.67 | 0.80 | 1.02 |
| 10-12 06:05 | +15 | HYPE | DOWN | 0.67 | 0.82 | 1.23 |
| 10-12 06:05 | +10 | HYPE | DOWN | 0.67 | 0.80 | 1.02 |
| 10-12 06:05 | +5 | HYPE | DOWN | 0.71 | 0.80 | 0.63 |
| 10-12 06:02 | +10 stop | DOGE | DOWN | 0.65 | 0.77 | 0.91 |
| 10-12 06:02 | +15 | DOGE | DOWN | 0.65 | 0.80 | 1.22 |
| 10-12 06:02 | +10 | DOGE | DOWN | 0.65 | 0.77 | 0.91 |
| 10-12 06:02 | +5 | DOGE | DOWN | 0.65 | 0.73 | 0.50 |
| 10-12 06:02 | +5 | BTC | DOWN | 0.66 | 0.71 | 0.19 |
| 10-12 06:02 | +10 stop | NEAR | DOWN | 0.54 | 0.31 | -2.63 |
| 10-12 06:02 | +5 | HYPE | DOWN | 0.53 | 0.58 | 0.14 |
| 10-12 06:02 | +10 stop | SOL | DOWN | 0.60 | 0.86 | 2.34 |
| 10-12 06:02 | +20 | SOL | DOWN | 0.60 | 0.86 | 2.34 |
| 10-12 06:02 | +15 | SOL | DOWN | 0.60 | 0.86 | 2.34 |
| 10-12 06:02 | +10 | SOL | DOWN | 0.60 | 0.86 | 2.34 |
| 10-12 06:02 | +5 | SOL | DOWN | 0.60 | 0.67 | 0.37 |
| 10-12 06:01 | +10 stop | ETH | DOWN | 0.67 | 0.82 | 1.23 |
| 10-12 06:01 | +20 | ETH | DOWN | 0.67 | 0.89 | 1.97 |
| 10-12 06:01 | +15 | ETH | DOWN | 0.67 | 0.82 | 1.23 |
| 10-12 06:01 | +10 | ETH | DOWN | 0.67 | 0.82 | 1.23 |
| 10-12 06:01 | +5 | ETH | DOWN | 0.67 | 0.72 | 0.19 |
| 10-12 06:01 | +10 stop | XRP | DOWN | 0.71 | 0.82 | 0.84 |
| 10-12 06:01 | +20 | XRP | DOWN | 0.71 | 0.92 | 1.88 |
| 10-12 06:01 | +15 | XRP | DOWN | 0.71 | 0.90 | 1.68 |
| 10-12 06:01 | +10 | XRP | DOWN | 0.71 | 0.82 | 0.84 |
| 10-12 06:01 | +5 | XRP | DOWN | 0.71 | 0.76 | 0.22 |
| 10-12 06:01 | +10 stop | NEAR | UP | 0.55 | 0.40 | -1.85 |
| 10-12 06:01 | +20 | NEAR | UP | 0.55 | open |  |
| 10-12 06:01 | +15 | NEAR | UP | 0.55 | 0.72 | 1.37 |
| 10-12 06:01 | +10 | NEAR | UP | 0.55 | 0.66 | 0.76 |
| 10-12 06:01 | +5 | NEAR | UP | 0.55 | 0.66 | 0.76 |
| 10-12 06:01 | +10 stop | BNB | DOWN | 0.69 | 0.85 | 1.36 |
| 10-12 06:01 | +20 | BNB | DOWN | 0.69 | 0.93 | 2.16 |
| 10-12 06:01 | +15 | BNB | DOWN | 0.69 | 0.85 | 1.36 |
