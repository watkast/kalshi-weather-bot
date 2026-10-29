# Range-Scalp Bot

*Updated Thu Oct 29 19:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 39633 | 34602 | 5031 (50) | 0 | $-11001.70 | -4.4% |
| **+10¢** | 29539 | 23721 | 5818 (73) | 0 | $-9764.09 | -5.3% |
| **+15¢** | 24699 | 18443 | 6256 (100) | 0 | $-8752.01 | -5.6% |
| **+20¢** | 21917 | 15364 | 6553 (129) | 0 | $-7630.20 | -5.5% |
| **+10¢ (15¢ stop)** | 48396 | 48326 | 70 (37) | 0 | $-18352.96 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-29 19:12 | +10 stop | BNB | DOWN | 0.66 | 0.83 | 1.44 |
| 10-29 19:12 | +20 | BNB | DOWN | 0.66 | 0.88 | 1.96 |
| 10-29 19:12 | +15 | BNB | DOWN | 0.66 | 0.83 | 1.44 |
| 10-29 19:12 | +10 | BNB | DOWN | 0.65 | 0.83 | 1.54 |
| 10-29 19:12 | +5 | BNB | DOWN | 0.65 | 0.71 | 0.29 |
| 10-29 19:05 | +10 stop | ETH | DOWN | 0.66 | 0.77 | 0.81 |
| 10-29 19:05 | +15 | ETH | DOWN | 0.66 | 0.82 | 1.33 |
| 10-29 19:05 | +10 | ETH | DOWN | 0.68 | 0.80 | 0.92 |
| 10-29 19:05 | +5 | ETH | DOWN | 0.69 | 0.77 | 0.52 |
| 10-29 19:04 | +15 | BTC | DOWN | 0.68 | 0.84 | 1.34 |
| 10-29 19:02 | +10 stop | BTC | DOWN | 0.70 | 0.80 | 0.73 |
| 10-29 19:02 | +10 | BTC | DOWN | 0.70 | 0.80 | 0.73 |
| 10-29 19:02 | +5 | BTC | DOWN | 0.70 | 0.76 | 0.32 |
| 10-29 19:01 | +5 | BTC | DOWN | 0.61 | 0.69 | 0.48 |
| 10-29 19:01 | +5 | ETH | DOWN | 0.68 | 0.77 | 0.61 |
| 10-29 19:01 | +10 stop | BTC | DOWN | 0.56 | 0.69 | 0.97 |
| 10-29 19:01 | +20 | BTC | DOWN | 0.56 | 0.76 | 1.69 |
| 10-29 19:01 | +15 | BTC | DOWN | 0.56 | 0.72 | 1.27 |
| 10-29 19:01 | +10 | BTC | DOWN | 0.56 | 0.69 | 0.97 |
| 10-29 19:01 | +5 | BTC | DOWN | 0.56 | 0.64 | 0.45 |
| 10-29 19:01 | +10 stop | ETH | DOWN | 0.63 | 0.77 | 1.10 |
| 10-29 19:01 | +20 | ETH | DOWN | 0.62 | 0.82 | 1.72 |
| 10-29 19:01 | +15 | ETH | DOWN | 0.63 | 0.80 | 1.41 |
| 10-29 19:01 | +10 | ETH | DOWN | 0.63 | 0.77 | 1.10 |
| 10-29 19:01 | +5 | ETH | DOWN | 0.62 | 0.69 | 0.38 |
| 10-29 19:01 | +10 stop | BNB | DOWN | 0.67 | 0.79 | 0.92 |
| 10-29 19:01 | +20 | BNB | DOWN | 0.67 | 0.87 | 1.76 |
| 10-29 19:01 | +15 | BNB | DOWN | 0.67 | 0.83 | 1.34 |
| 10-29 19:01 | +10 | BNB | DOWN | 0.67 | 0.79 | 0.92 |
| 10-29 19:01 | +5 | BNB | DOWN | 0.67 | 0.73 | 0.30 |
| 10-29 19:01 | +10 stop | DOGE | DOWN | 0.71 | 0.83 | 0.95 |
| 10-29 19:01 | +20 | DOGE | DOWN | 0.71 | 0.91 | 1.83 |
| 10-29 19:01 | +15 | DOGE | DOWN | 0.71 | 0.86 | 1.26 |
| 10-29 19:01 | +10 | DOGE | DOWN | 0.71 | 0.83 | 0.95 |
| 10-29 19:01 | +5 | DOGE | DOWN | 0.71 | 0.77 | 0.32 |
| 10-29 18:52 | +10 stop | ZEC | UP | 0.67 | 0.80 | 1.02 |
| 10-29 18:52 | +10 stop | BNB | UP | 0.63 | 0.74 | 0.79 |
| 10-29 18:52 | +15 | BNB | UP | 0.63 | 0.86 | 2.04 |
| 10-29 18:52 | +10 | BNB | UP | 0.63 | 0.74 | 0.79 |
| 10-29 18:52 | +10 stop | ZEC | UP | 0.53 | 0.63 | 0.65 |
