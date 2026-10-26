# Range-Scalp Bot

*Updated Mon Oct 26 13:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 34922 | 30497 | 4425 (43) | 3 | $-9628.61 | -4.4% |
| **+10¢** | 26129 | 21012 | 5117 (65) | 4 | $-8421.70 | -5.1% |
| **+15¢** | 21865 | 16355 | 5510 (89) | 4 | $-7524.77 | -5.5% |
| **+20¢** | 19379 | 13603 | 5776 (112) | 4 | $-6614.56 | -5.4% |
| **+10¢ (15¢ stop)** | 42723 | 42661 | 62 (33) | 0 | $-16192.48 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-26 13:54 | +10 stop | NEAR | DOWN | 0.64 | 0.43 | -2.45 |
| 10-26 13:52 | +5 | XRP | DOWN | 0.65 | 0.72 | 0.39 |
| 10-26 13:52 | +10 stop | SOL | DOWN | 0.64 | 0.74 | 0.69 |
| 10-26 13:52 | +10 stop | BNB | DOWN | 0.62 | 0.82 | 1.72 |
| 10-26 13:52 | +10 stop | HYPE | DOWN | 0.70 | 0.83 | 1.05 |
| 10-26 13:52 | +10 stop | NEAR | DOWN | 0.55 | 0.65 | 0.66 |
| 10-26 13:52 | +5 | ETH | DOWN | 0.59 | 0.66 | 0.34 |
| 10-26 13:52 | +15 | XRP | DOWN | 0.59 | 0.78 | 1.61 |
| 10-26 13:52 | +5 | XRP | DOWN | 0.59 | 0.65 | 0.28 |
| 10-26 13:52 | +5 | DOGE | DOWN | 0.61 | 0.67 | 0.27 |
| 10-26 13:51 | +5 | ZEC | DOWN | 0.52 | 0.61 | 0.55 |
| 10-26 13:51 | +5 | DOGE | DOWN | 0.61 | 0.67 | 0.27 |
| 10-26 13:51 | +10 stop | BNB | DOWN | 0.66 | 0.49 | -2.04 |
| 10-26 13:51 | +20 | BNB | DOWN | 0.66 | 0.86 | 1.75 |
| 10-26 13:51 | +15 | BNB | DOWN | 0.66 | 0.82 | 1.33 |
| 10-26 13:51 | +10 | BNB | DOWN | 0.66 | 0.82 | 1.35 |
| 10-26 13:51 | +5 | BNB | DOWN | 0.66 | 0.82 | 1.35 |
| 10-26 13:50 | +5 | ZEC | DOWN | 0.65 | 0.70 | 0.19 |
| 10-26 13:50 | +10 stop | DOGE | DOWN | 0.66 | 0.81 | 1.23 |
| 10-26 13:50 | +10 | DOGE | DOWN | 0.66 | 0.81 | 1.23 |
| 10-26 13:50 | +5 | DOGE | DOWN | 0.66 | 0.73 | 0.40 |
| 10-26 13:50 | +10 stop | BTC | DOWN | 0.54 | 0.69 | 1.17 |
| 10-26 13:50 | +10 stop | HYPE | DOWN | 0.55 | 0.33 | -2.54 |
| 10-26 13:50 | +10 stop | XRP | DOWN | 0.63 | 0.78 | 1.20 |
| 10-26 13:50 | +10 | XRP | DOWN | 0.64 | 0.78 | 1.10 |
| 10-26 13:50 | +5 | XRP | DOWN | 0.65 | 0.71 | 0.29 |
| 10-26 13:49 | +10 stop | ETH | DOWN | 0.66 | 0.79 | 1.02 |
| 10-26 13:49 | +5 | ETH | DOWN | 0.66 | 0.73 | 0.40 |
| 10-26 13:49 | +10 stop | SOL | DOWN | 0.67 | 0.50 | -2.04 |
| 10-26 13:49 | +10 stop | NEAR | DOWN | 0.65 | 0.50 | -1.84 |
| 10-26 13:49 | +10 stop | HYPE | UP | 0.60 | 0.37 | -2.64 |
| 10-26 13:49 | +10 stop | DOGE | DOWN | 0.57 | 0.71 | 1.07 |
| 10-26 13:49 | +10 | DOGE | DOWN | 0.57 | 0.71 | 1.07 |
| 10-26 13:49 | +5 | DOGE | DOWN | 0.57 | 0.65 | 0.46 |
| 10-26 13:48 | +10 stop | ZEC | DOWN | 0.64 | 0.48 | -1.95 |
| 10-26 13:48 | +15 | ZEC | DOWN | 0.64 | 0.80 | 1.31 |
| 10-26 13:48 | +10 | ZEC | DOWN | 0.64 | 0.76 | 0.90 |
| 10-26 13:48 | +5 | ZEC | DOWN | 0.64 | 0.71 | 0.38 |
| 10-26 13:48 | +10 stop | XRP | DOWN | 0.56 | 0.67 | 0.76 |
| 10-26 13:48 | +20 | XRP | DOWN | 0.56 | 0.78 | 1.89 |
