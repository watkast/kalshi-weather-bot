# Range-Scalp Bot

*Updated Thu Nov 19 18:52 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 65375 | 57081 | 8294 (124) | 1 | $-17402.68 | -4.2% |
| **+10¢** | 48815 | 39107 | 9708 (165) | 1 | $-16228.89 | -5.3% |
| **+15¢** | 40934 | 30462 | 10472 (211) | 1 | $-14606.08 | -5.7% |
| **+20¢** | 36451 | 25448 | 11003 (266) | 1 | $-12925.27 | -5.7% |
| **+10¢ (15¢ stop)** | 79576 | 79412 | 164 (98) | 0 | $-29282.53 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-19 18:49 | +10 stop | DOGE | DOWN | 0.62 | 0.77 | 1.18 |
| 11-19 18:47 | +10 stop | ETH | DOWN | 0.66 | 0.79 | 1.02 |
| 11-19 18:47 | +20 | ETH | DOWN | 0.65 | 0.85 | 1.75 |
| 11-19 18:47 | +15 | ETH | DOWN | 0.65 | 0.84 | 1.64 |
| 11-19 18:47 | +10 | ETH | DOWN | 0.65 | 0.79 | 1.12 |
| 11-19 18:47 | +5 | ETH | DOWN | 0.65 | 0.71 | 0.29 |
| 11-19 18:47 | +5 | NEAR | DOWN | 0.71 | 0.78 | 0.42 |
| 11-19 18:47 | +10 stop | SOL | DOWN | 0.63 | 0.74 | 0.79 |
| 11-19 18:47 | +20 | SOL | DOWN | 0.62 | 0.83 | 1.83 |
| 11-19 18:47 | +15 | SOL | DOWN | 0.63 | 0.78 | 1.20 |
| 11-19 18:47 | +10 | SOL | DOWN | 0.62 | 0.74 | 0.89 |
| 11-19 18:47 | +5 | SOL | DOWN | 0.61 | 0.66 | 0.17 |
| 11-19 18:47 | +10 stop | ZEC | DOWN | 0.58 | 0.71 | 0.97 |
| 11-19 18:47 | +20 | ZEC | DOWN | 0.58 | 0.86 | 2.53 |
| 11-19 18:47 | +15 | ZEC | DOWN | 0.58 | 0.74 | 1.28 |
| 11-19 18:47 | +10 | ZEC | DOWN | 0.58 | 0.71 | 0.97 |
| 11-19 18:47 | +5 | ZEC | DOWN | 0.58 | 0.71 | 0.97 |
| 11-19 18:47 | +10 stop | BTC | DOWN | 0.60 | 0.72 | 0.88 |
| 11-19 18:47 | +20 | BTC | DOWN | 0.59 | 0.80 | 1.81 |
| 11-19 18:47 | +15 | BTC | DOWN | 0.59 | 0.74 | 1.19 |
| 11-19 18:47 | +10 | BTC | DOWN | 0.59 | 0.72 | 0.98 |
| 11-19 18:47 | +5 | BTC | DOWN | 0.59 | 0.68 | 0.57 |
| 11-19 18:46 | +10 stop | HYPE | DOWN | 0.71 | 0.81 | 0.74 |
| 11-19 18:46 | +20 | HYPE | DOWN | 0.71 | 0.92 | 1.88 |
| 11-19 18:46 | +15 | HYPE | DOWN | 0.71 | 0.88 | 1.47 |
| 11-19 18:46 | +10 | HYPE | DOWN | 0.71 | 0.81 | 0.74 |
| 11-19 18:46 | +5 | HYPE | DOWN | 0.71 | 0.80 | 0.63 |
| 11-19 18:46 | +10 stop | NEAR | DOWN | 0.59 | 0.70 | 0.78 |
| 11-19 18:46 | +20 | NEAR | DOWN | 0.59 | 0.79 | 1.71 |
| 11-19 18:46 | +15 | NEAR | DOWN | 0.59 | 0.74 | 1.19 |
| 11-19 18:46 | +10 | NEAR | DOWN | 0.59 | 0.70 | 0.78 |
| 11-19 18:46 | +5 | NEAR | DOWN | 0.59 | 0.65 | 0.27 |
| 11-19 18:46 | +10 stop | BNB | DOWN | 0.56 | 0.72 | 1.27 |
| 11-19 18:46 | +20 | BNB | DOWN | 0.56 | 0.76 | 1.69 |
| 11-19 18:46 | +15 | BNB | DOWN | 0.57 | 0.72 | 1.17 |
| 11-19 18:46 | +10 | BNB | DOWN | 0.57 | 0.72 | 1.17 |
| 11-19 18:46 | +5 | BNB | DOWN | 0.57 | 0.64 | 0.35 |
| 11-19 18:46 | +10 stop | XRP | DOWN | 0.64 | 0.76 | 0.91 |
| 11-19 18:46 | +20 | XRP | DOWN | 0.64 | 0.88 | 2.11 |
| 11-19 18:46 | +15 | XRP | DOWN | 0.62 | 0.81 | 1.62 |
