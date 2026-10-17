# Range-Scalp Bot

*Updated Sat Oct 17 17:05 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 21283 | 18532 | 2751 (29) | 3 | $-6159.62 | -4.6% |
| **+10¢** | 16012 | 12833 | 3179 (41) | 2 | $-5499.05 | -5.5% |
| **+15¢** | 13387 | 9963 | 3424 (61) | 2 | $-4983.09 | -5.9% |
| **+20¢** | 11860 | 8273 | 3587 (80) | 5 | $-4426.29 | -5.9% |
| **+10¢ (15¢ stop)** | 26127 | 26077 | 50 (29) | 2 | $-9936.38 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 17:04 | +10 stop | DOGE | DOWN | 0.69 | 0.82 | 1.04 |
| 10-17 17:04 | +10 stop | BTC | DOWN | 0.65 | 0.75 | 0.70 |
| 10-17 17:04 | +5 | BTC | DOWN | 0.65 | 0.75 | 0.70 |
| 10-17 17:04 | +10 stop | SOL | DOWN | 0.67 | open |  |
| 10-17 17:04 | +10 stop | XRP | DOWN | 0.70 | open |  |
| 10-17 17:03 | +10 stop | DOGE | UP | 0.34 | 0.65 | 2.78 |
| 10-17 17:03 | +10 stop | ETH | UP | 0.46 | 0.28 | -2.13 |
| 10-17 17:03 | +10 | ETH | UP | 0.49 | open |  |
| 10-17 17:03 | +5 | ETH | UP | 0.51 | open |  |
| 10-17 17:03 | +10 stop | XRP | UP | 0.68 | 0.44 | -2.74 |
| 10-17 17:03 | +5 | DOGE | UP | 0.68 | open |  |
| 10-17 17:03 | +5 | NEAR | DOWN | 0.59 | 0.68 | 0.57 |
| 10-17 17:03 | +5 | BTC | DOWN | 0.50 | 0.61 | 0.75 |
| 10-17 17:02 | +10 stop | DOGE | DOWN | 0.55 | 0.33 | -2.54 |
| 10-17 17:02 | +5 | DOGE | DOWN | 0.56 | 0.61 | 0.15 |
| 10-17 17:02 | +5 | HYPE | DOWN | 0.65 | 0.87 | 1.92 |
| 10-17 17:02 | +5 | XRP | DOWN | 0.61 | 0.68 | 0.37 |
| 10-17 17:02 | +5 | BTC | DOWN | 0.60 | 0.66 | 0.27 |
| 10-17 17:01 | +10 stop | ETH | DOWN | 0.50 | 0.61 | 0.75 |
| 10-17 17:01 | +20 | ETH | DOWN | 0.51 | 0.71 | 1.67 |
| 10-17 17:01 | +15 | ETH | DOWN | 0.51 | 0.71 | 1.67 |
| 10-17 17:01 | +10 | ETH | DOWN | 0.51 | 0.61 | 0.65 |
| 10-17 17:01 | +5 | ETH | DOWN | 0.51 | 0.61 | 0.65 |
| 10-17 17:01 | +10 stop | HYPE | DOWN | 0.59 | 0.87 | 2.55 |
| 10-17 17:01 | +20 | HYPE | DOWN | 0.59 | 0.87 | 2.55 |
| 10-17 17:01 | +15 | HYPE | DOWN | 0.59 | 0.87 | 2.55 |
| 10-17 17:01 | +10 | HYPE | DOWN | 0.59 | 0.87 | 2.55 |
| 10-17 17:01 | +5 | HYPE | DOWN | 0.59 | 0.66 | 0.37 |
| 10-17 17:01 | +10 stop | BTC | DOWN | 0.63 | 0.47 | -1.95 |
| 10-17 17:01 | +20 | BTC | DOWN | 0.63 | open |  |
| 10-17 17:01 | +15 | BTC | DOWN | 0.63 | open |  |
| 10-17 17:01 | +10 | BTC | DOWN | 0.63 | 0.75 | 0.89 |
| 10-17 17:01 | +5 | BTC | DOWN | 0.63 | 0.68 | 0.17 |
| 10-17 17:01 | +10 stop | BNB | DOWN | 0.64 | 0.78 | 1.10 |
| 10-17 17:01 | +20 | BNB | DOWN | 0.64 | 0.84 | 1.73 |
| 10-17 17:01 | +15 | BNB | DOWN | 0.64 | 0.84 | 1.73 |
| 10-17 17:01 | +10 | BNB | DOWN | 0.64 | 0.78 | 1.10 |
| 10-17 17:01 | +5 | BNB | DOWN | 0.64 | 0.78 | 1.10 |
| 10-17 17:01 | +10 stop | DOGE | DOWN | 0.66 | 0.51 | -1.84 |
| 10-17 17:01 | +20 | DOGE | DOWN | 0.66 | open |  |
