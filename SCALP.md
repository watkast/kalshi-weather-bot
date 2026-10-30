# Range-Scalp Bot

*Updated Fri Oct 30 00:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 39950 | 34897 | 5053 (51) | 0 | $-10934.32 | -4.3% |
| **+10¢** | 29775 | 23931 | 5844 (74) | 0 | $-9662.63 | -5.2% |
| **+15¢** | 24896 | 18609 | 6287 (101) | 0 | $-8654.00 | -5.5% |
| **+20¢** | 22091 | 15499 | 6592 (130) | 0 | $-7570.56 | -5.5% |
| **+10¢ (15¢ stop)** | 48756 | 48686 | 70 (37) | 0 | $-18417.93 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-30 00:21 | +5 | NEAR | DOWN | 0.71 | 0.91 | 1.80 |
| 10-30 00:19 | +5 | HYPE | DOWN | 0.67 | 0.74 | 0.40 |
| 10-30 00:18 | +5 | ETH | DOWN | 0.71 | 0.94 | 2.16 |
| 10-30 00:16 | +10 stop | DOGE | DOWN | 0.64 | 0.76 | 0.90 |
| 10-30 00:16 | +20 | DOGE | DOWN | 0.64 | 0.97 | 3.06 |
| 10-30 00:16 | +15 | DOGE | DOWN | 0.64 | 0.97 | 3.06 |
| 10-30 00:16 | +10 | DOGE | DOWN | 0.62 | 0.76 | 1.10 |
| 10-30 00:16 | +5 | DOGE | DOWN | 0.63 | 0.69 | 0.28 |
| 10-30 00:16 | +5 | BTC | DOWN | 0.62 | 0.74 | 0.89 |
| 10-30 00:16 | +5 | SOL | DOWN | 0.67 | 0.76 | 0.61 |
| 10-30 00:16 | +10 stop | ETH | DOWN | 0.61 | 0.94 | 3.14 |
| 10-30 00:16 | +20 | ETH | DOWN | 0.61 | 0.94 | 3.14 |
| 10-30 00:16 | +15 | ETH | DOWN | 0.61 | 0.94 | 3.14 |
| 10-30 00:16 | +10 | ETH | DOWN | 0.61 | 0.94 | 3.14 |
| 10-30 00:16 | +5 | ETH | DOWN | 0.61 | 0.67 | 0.27 |
| 10-30 00:16 | +10 stop | BNB | DOWN | 0.66 | 0.77 | 0.81 |
| 10-30 00:16 | +20 | BNB | DOWN | 0.66 | 0.86 | 1.75 |
| 10-30 00:16 | +15 | BNB | DOWN | 0.66 | 0.83 | 1.44 |
| 10-30 00:16 | +10 | BNB | DOWN | 0.66 | 0.77 | 0.81 |
| 10-30 00:16 | +5 | BNB | DOWN | 0.66 | 0.73 | 0.40 |
| 10-30 00:16 | +10 stop | ZEC | DOWN | 0.65 | 0.80 | 1.22 |
| 10-30 00:16 | +20 | ZEC | DOWN | 0.64 | 0.85 | 1.84 |
| 10-30 00:16 | +15 | ZEC | DOWN | 0.63 | 0.80 | 1.41 |
| 10-30 00:16 | +10 | ZEC | DOWN | 0.63 | 0.80 | 1.41 |
| 10-30 00:16 | +5 | ZEC | DOWN | 0.63 | 0.80 | 1.41 |
| 10-30 00:16 | +10 stop | HYPE | DOWN | 0.57 | 0.74 | 1.38 |
| 10-30 00:16 | +20 | HYPE | DOWN | 0.57 | 0.78 | 1.79 |
| 10-30 00:16 | +15 | HYPE | DOWN | 0.57 | 0.74 | 1.38 |
| 10-30 00:16 | +10 | HYPE | DOWN | 0.57 | 0.74 | 1.38 |
| 10-30 00:16 | +5 | HYPE | DOWN | 0.57 | 0.62 | 0.15 |
| 10-30 00:16 | +10 stop | XRP | DOWN | 0.65 | 0.78 | 1.01 |
| 10-30 00:16 | +20 | XRP | DOWN | 0.65 | 0.94 | 2.71 |
| 10-30 00:16 | +15 | XRP | DOWN | 0.65 | 0.84 | 1.64 |
| 10-30 00:16 | +10 | XRP | DOWN | 0.65 | 0.78 | 1.01 |
| 10-30 00:16 | +5 | XRP | DOWN | 0.65 | 0.70 | 0.19 |
| 10-30 00:16 | +10 stop | BTC | DOWN | 0.57 | 0.74 | 1.38 |
| 10-30 00:16 | +20 | BTC | DOWN | 0.57 | 0.83 | 2.32 |
| 10-30 00:16 | +15 | BTC | DOWN | 0.57 | 0.74 | 1.38 |
| 10-30 00:16 | +10 | BTC | DOWN | 0.57 | 0.74 | 1.38 |
| 10-30 00:16 | +5 | BTC | DOWN | 0.57 | 0.63 | 0.25 |
