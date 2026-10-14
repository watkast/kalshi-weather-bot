# Range-Scalp Bot

*Updated Wed Oct 14 19:07 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 16394 | 14201 | 2193 (28) | 0 | $-5192.03 | -5.0% |
| **+10¢** | 12402 | 9861 | 2541 (40) | 0 | $-4773.74 | -6.1% |
| **+15¢** | 10424 | 7696 | 2728 (59) | 0 | $-4281.91 | -6.5% |
| **+20¢** | 9268 | 6408 | 2860 (76) | 1 | $-3797.63 | -6.5% |
| **+10¢ (15¢ stop)** | 20202 | 20152 | 50 (29) | 0 | $-7792.53 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-14 19:02 | +5 | XRP | UP | 0.45 | 0.54 | 0.54 |
| 10-14 19:02 | +10 stop | ETH | DOWN | 0.63 | 0.74 | 0.79 |
| 10-14 19:02 | +10 | ETH | DOWN | 0.63 | 0.74 | 0.79 |
| 10-14 19:02 | +5 | ETH | DOWN | 0.63 | 0.74 | 0.79 |
| 10-14 19:02 | +10 stop | BTC | DOWN | 0.58 | 0.77 | 1.59 |
| 10-14 19:02 | +20 | BTC | DOWN | 0.58 | 0.78 | 1.69 |
| 10-14 19:02 | +15 | BTC | DOWN | 0.58 | 0.77 | 1.59 |
| 10-14 19:02 | +10 | BTC | DOWN | 0.58 | 0.77 | 1.59 |
| 10-14 19:02 | +5 | BTC | DOWN | 0.57 | 0.64 | 0.35 |
| 10-14 19:02 | +10 stop | HYPE | DOWN | 0.70 | 0.84 | 1.15 |
| 10-14 19:02 | +20 | HYPE | DOWN | 0.70 | 0.92 | 2.04 |
| 10-14 19:02 | +15 | HYPE | DOWN | 0.70 | 0.86 | 1.36 |
| 10-14 19:02 | +10 | HYPE | DOWN | 0.70 | 0.84 | 1.15 |
| 10-14 19:02 | +5 | HYPE | DOWN | 0.70 | 0.79 | 0.63 |
| 10-14 19:02 | +10 stop | BNB | DOWN | 0.63 | 0.73 | 0.69 |
| 10-14 19:02 | +10 | BNB | DOWN | 0.63 | 0.73 | 0.69 |
| 10-14 19:02 | +5 | BNB | DOWN | 0.63 | 0.68 | 0.17 |
| 10-14 19:02 | +5 | XRP | DOWN | 0.51 | 0.59 | 0.45 |
| 10-14 19:02 | +10 stop | XRP | DOWN | 0.51 | 0.71 | 1.67 |
| 10-14 19:01 | +10 stop | NEAR | DOWN | 0.71 | 0.82 | 0.87 |
| 10-14 19:01 | +20 | NEAR | DOWN | 0.71 | open |  |
| 10-14 19:01 | +15 | NEAR | DOWN | 0.71 | 0.86 | 1.29 |
| 10-14 19:01 | +10 | NEAR | DOWN | 0.71 | 0.82 | 0.87 |
| 10-14 19:01 | +5 | NEAR | DOWN | 0.71 | 0.79 | 0.56 |
| 10-14 19:01 | +10 stop | ZEC | DOWN | 0.68 | 0.79 | 0.80 |
| 10-14 19:01 | +20 | ZEC | DOWN | 0.68 | 0.92 | 2.12 |
| 10-14 19:01 | +15 | ZEC | DOWN | 0.68 | 0.86 | 1.52 |
| 10-14 19:01 | +10 | ZEC | DOWN | 0.68 | 0.79 | 0.80 |
| 10-14 19:01 | +5 | ZEC | DOWN | 0.68 | 0.79 | 0.80 |
| 10-14 19:01 | +10 stop | ETH | DOWN | 0.54 | 0.65 | 0.76 |
| 10-14 19:01 | +20 | ETH | DOWN | 0.54 | 0.74 | 1.68 |
| 10-14 19:01 | +15 | ETH | DOWN | 0.55 | 0.74 | 1.58 |
| 10-14 19:01 | +10 | ETH | DOWN | 0.55 | 0.65 | 0.66 |
| 10-14 19:01 | +5 | ETH | DOWN | 0.55 | 0.65 | 0.66 |
| 10-14 19:01 | +10 stop | BNB | DOWN | 0.58 | 0.69 | 0.73 |
| 10-14 19:01 | +20 | BNB | DOWN | 0.58 | 0.83 | 2.18 |
| 10-14 19:01 | +15 | BNB | DOWN | 0.58 | 0.83 | 2.18 |
| 10-14 19:01 | +10 | BNB | DOWN | 0.58 | 0.69 | 0.73 |
| 10-14 19:01 | +5 | BNB | DOWN | 0.58 | 0.69 | 0.73 |
| 10-14 19:01 | +10 stop | SOL | DOWN | 0.64 | 0.77 | 1.00 |
