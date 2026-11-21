# Range-Scalp Bot

*Updated Sat Nov 21 17:39 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 67670 | 59056 | 8614 (134) | 0 | $-18195.72 | -4.3% |
| **+10¢** | 50534 | 40471 | 10063 (175) | 0 | $-16884.79 | -5.3% |
| **+15¢** | 42365 | 31517 | 10848 (225) | 0 | $-15137.53 | -5.7% |
| **+20¢** | 37710 | 26311 | 11399 (283) | 0 | $-13451.65 | -5.7% |
| **+10¢ (15¢ stop)** | 82376 | 82205 | 171 (105) | 0 | $-30230.59 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-21 17:36 | +10 stop | HYPE | DOWN | 0.59 | 0.75 | 1.32 |
| 11-21 17:35 | +5 | HYPE | DOWN | 0.69 | 0.75 | 0.29 |
| 11-21 17:34 | +10 stop | HYPE | DOWN | 0.63 | 0.48 | -1.85 |
| 11-21 17:34 | +20 | HYPE | DOWN | 0.63 | 0.85 | 1.94 |
| 11-21 17:34 | +15 | HYPE | DOWN | 0.63 | 0.81 | 1.52 |
| 11-21 17:34 | +10 | HYPE | DOWN | 0.63 | 0.75 | 0.89 |
| 11-21 17:34 | +5 | HYPE | DOWN | 0.64 | 0.69 | 0.18 |
| 11-21 17:32 | +10 stop | HYPE | DOWN | 0.64 | 0.77 | 1.00 |
| 11-21 17:32 | +10 | HYPE | DOWN | 0.64 | 0.77 | 1.00 |
| 11-21 17:31 | +5 | HYPE | DOWN | 0.65 | 0.73 | 0.50 |
| 11-21 17:31 | +5 | NEAR | DOWN | 0.65 | 0.90 | 2.27 |
| 11-21 17:31 | +10 stop | HYPE | DOWN | 0.55 | 0.66 | 0.76 |
| 11-21 17:31 | +20 | HYPE | DOWN | 0.55 | 0.77 | 1.89 |
| 11-21 17:31 | +15 | HYPE | DOWN | 0.55 | 0.73 | 1.48 |
| 11-21 17:31 | +10 | HYPE | DOWN | 0.55 | 0.66 | 0.76 |
| 11-21 17:31 | +5 | HYPE | DOWN | 0.55 | 0.62 | 0.35 |
| 11-21 17:31 | +10 stop | ZEC | DOWN | 0.62 | 0.76 | 1.10 |
| 11-21 17:31 | +20 | ZEC | DOWN | 0.62 | 0.82 | 1.72 |
| 11-21 17:31 | +15 | ZEC | DOWN | 0.62 | 0.81 | 1.62 |
| 11-21 17:31 | +10 | ZEC | DOWN | 0.62 | 0.76 | 1.10 |
| 11-21 17:31 | +5 | ZEC | DOWN | 0.62 | 0.68 | 0.27 |
| 11-21 17:31 | +10 stop | NEAR | DOWN | 0.60 | 0.45 | -1.85 |
| 11-21 17:31 | +20 | NEAR | DOWN | 0.60 | 0.90 | 2.76 |
| 11-21 17:31 | +15 | NEAR | DOWN | 0.60 | 0.90 | 2.76 |
| 11-21 17:31 | +10 | NEAR | DOWN | 0.60 | 0.90 | 2.76 |
| 11-21 17:31 | +5 | NEAR | DOWN | 0.60 | 0.67 | 0.37 |
| 11-21 17:29 | +10 stop | BTC | UP | 0.39 | 0.54 | 1.15 |
| 11-21 17:28 | +5 | ETH | DOWN | 0.64 | 0.89 | 2.26 |
| 11-21 17:28 | +10 stop | ETH | DOWN | 0.52 | 0.68 | 1.26 |
| 11-21 17:28 | +20 | ETH | DOWN | 0.52 | 0.89 | 3.45 |
| 11-21 17:28 | +15 | ETH | DOWN | 0.52 | 0.68 | 1.26 |
| 11-21 17:28 | +10 | ETH | DOWN | 0.52 | 0.68 | 1.26 |
| 11-21 17:28 | +5 | ETH | DOWN | 0.52 | 0.59 | 0.37 |
| 11-21 17:28 | +10 stop | SOL | DOWN | 0.50 | 0.63 | 0.95 |
| 11-21 17:27 | +10 stop | BTC | DOWN | 0.64 | 0.38 | -2.94 |
| 11-21 17:27 | +20 | BTC | DOWN | 0.64 | yes | -6.57 |
| 11-21 17:27 | +15 | BTC | DOWN | 0.64 | yes | -6.57 |
| 11-21 17:27 | +10 | BTC | DOWN | 0.64 | yes | -6.57 |
| 11-21 17:27 | +5 | BTC | DOWN | 0.64 | yes | -6.57 |
| 11-21 17:27 | +10 stop | SOL | DOWN | 0.67 | 0.44 | -2.64 |
