# Range-Scalp Bot

*Updated Fri Nov 06 07:06 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 49352 | 43005 | 6347 (75) | 0 | $-13986.25 | -4.5% |
| **+10¢** | 36844 | 29465 | 7379 (101) | 0 | $-12851.76 | -5.5% |
| **+15¢** | 30863 | 22918 | 7945 (130) | 0 | $-11722.56 | -6.1% |
| **+20¢** | 27436 | 19110 | 8326 (170) | 0 | $-10354.24 | -6.0% |
| **+10¢ (15¢ stop)** | 60166 | 60071 | 95 (57) | 0 | $-22284.12 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-06 07:01 | +10 stop | BTC | DOWN | 0.62 | 0.86 | 2.14 |
| 11-06 07:01 | +20 | BTC | DOWN | 0.62 | 0.86 | 2.14 |
| 11-06 07:01 | +15 | BTC | DOWN | 0.62 | 0.86 | 2.14 |
| 11-06 07:01 | +10 | BTC | DOWN | 0.62 | 0.86 | 2.14 |
| 11-06 07:01 | +5 | BTC | DOWN | 0.62 | 0.70 | 0.48 |
| 11-06 07:01 | +10 stop | HYPE | DOWN | 0.64 | 0.80 | 1.31 |
| 11-06 07:01 | +20 | HYPE | DOWN | 0.64 | 0.84 | 1.73 |
| 11-06 07:01 | +15 | HYPE | DOWN | 0.64 | 0.80 | 1.31 |
| 11-06 07:01 | +10 | HYPE | DOWN | 0.64 | 0.80 | 1.31 |
| 11-06 07:01 | +5 | HYPE | DOWN | 0.64 | 0.70 | 0.28 |
| 11-06 07:01 | +10 stop | XRP | DOWN | 0.59 | 0.73 | 1.09 |
| 11-06 07:01 | +20 | XRP | DOWN | 0.59 | 0.80 | 1.81 |
| 11-06 07:01 | +15 | XRP | DOWN | 0.59 | 0.80 | 1.81 |
| 11-06 07:01 | +10 | XRP | DOWN | 0.59 | 0.73 | 1.09 |
| 11-06 07:01 | +5 | XRP | DOWN | 0.59 | 0.73 | 1.09 |
| 11-06 07:01 | +10 stop | BNB | DOWN | 0.69 | 0.81 | 0.94 |
| 11-06 07:01 | +20 | BNB | DOWN | 0.69 | 0.93 | 2.22 |
| 11-06 07:01 | +15 | BNB | DOWN | 0.69 | 0.86 | 1.46 |
| 11-06 07:01 | +10 | BNB | DOWN | 0.69 | 0.81 | 0.94 |
| 11-06 07:01 | +5 | BNB | DOWN | 0.69 | 0.74 | 0.21 |
| 11-06 07:01 | +10 stop | ETH | DOWN | 0.67 | 0.78 | 0.81 |
| 11-06 07:01 | +20 | ETH | DOWN | 0.67 | 0.87 | 1.76 |
| 11-06 07:01 | +15 | ETH | DOWN | 0.67 | 0.87 | 1.76 |
| 11-06 07:01 | +10 | ETH | DOWN | 0.67 | 0.78 | 0.81 |
| 11-06 07:01 | +5 | ETH | DOWN | 0.67 | 0.78 | 0.81 |
| 11-06 07:01 | +10 stop | DOGE | DOWN | 0.63 | 0.78 | 1.20 |
| 11-06 07:01 | +20 | DOGE | DOWN | 0.63 | 0.85 | 1.94 |
| 11-06 07:01 | +15 | DOGE | DOWN | 0.63 | 0.78 | 1.20 |
| 11-06 07:01 | +10 | DOGE | DOWN | 0.63 | 0.78 | 1.20 |
| 11-06 07:01 | +5 | DOGE | DOWN | 0.63 | 0.78 | 1.20 |
| 11-06 07:00 | +10 stop | SOL | DOWN | 0.56 | 0.69 | 0.97 |
| 11-06 07:00 | +20 | SOL | DOWN | 0.56 | 0.77 | 1.79 |
| 11-06 07:00 | +15 | SOL | DOWN | 0.56 | 0.73 | 1.38 |
| 11-06 07:00 | +10 | SOL | DOWN | 0.56 | 0.69 | 0.97 |
| 11-06 07:00 | +5 | SOL | DOWN | 0.56 | 0.69 | 0.97 |
| 11-06 06:58 | +10 stop | BTC | UP | 0.51 | 0.62 | 0.75 |
| 11-06 06:58 | +15 | BTC | UP | 0.51 | 0.92 | 3.82 |
| 11-06 06:58 | +10 | BTC | UP | 0.51 | 0.62 | 0.75 |
| 11-06 06:58 | +5 | BTC | UP | 0.51 | 0.62 | 0.75 |
| 11-06 06:57 | +10 stop | ETH | UP | 0.54 | 0.65 | 0.76 |
