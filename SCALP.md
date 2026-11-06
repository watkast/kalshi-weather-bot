# Range-Scalp Bot

*Updated Fri Nov 06 12:52 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 49467 | 43105 | 6362 (76) | 0 | $-14013.73 | -4.5% |
| **+10¢** | 36929 | 29532 | 7397 (101) | 0 | $-12890.18 | -5.6% |
| **+15¢** | 30936 | 22971 | 7965 (130) | 0 | $-11764.87 | -6.1% |
| **+20¢** | 27504 | 19156 | 8348 (171) | 0 | $-10387.07 | -6.0% |
| **+10¢ (15¢ stop)** | 60303 | 60206 | 97 (57) | 0 | $-22353.31 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-06 12:48 | +5 | BNB | DOWN | 0.63 | 0.69 | 0.28 |
| 11-06 12:47 | +5 | SOL | DOWN | 0.68 | 0.76 | 0.51 |
| 11-06 12:47 | +10 stop | BNB | DOWN | 0.55 | 0.69 | 1.07 |
| 11-06 12:47 | +20 | BNB | DOWN | 0.56 | 0.77 | 1.79 |
| 11-06 12:47 | +15 | BNB | DOWN | 0.56 | 0.75 | 1.58 |
| 11-06 12:47 | +10 | BNB | DOWN | 0.57 | 0.69 | 0.87 |
| 11-06 12:47 | +5 | BNB | DOWN | 0.57 | 0.63 | 0.25 |
| 11-06 12:47 | +10 stop | ZEC | DOWN | 0.68 | 0.82 | 1.13 |
| 11-06 12:47 | +20 | ZEC | DOWN | 0.68 | 0.91 | 2.08 |
| 11-06 12:47 | +15 | ZEC | DOWN | 0.68 | 0.86 | 1.55 |
| 11-06 12:47 | +10 | ZEC | DOWN | 0.68 | 0.82 | 1.13 |
| 11-06 12:47 | +5 | ZEC | DOWN | 0.68 | 0.75 | 0.40 |
| 11-06 12:47 | +10 stop | BTC | DOWN | 0.58 | 0.70 | 0.87 |
| 11-06 12:47 | +20 | BTC | DOWN | 0.58 | 0.81 | 2.01 |
| 11-06 12:47 | +15 | BTC | DOWN | 0.58 | 0.75 | 1.38 |
| 11-06 12:47 | +10 | BTC | DOWN | 0.58 | 0.70 | 0.87 |
| 11-06 12:47 | +5 | BTC | DOWN | 0.58 | 0.64 | 0.25 |
| 11-06 12:46 | +10 stop | SOL | DOWN | 0.56 | 0.66 | 0.66 |
| 11-06 12:46 | +20 | SOL | DOWN | 0.56 | 0.76 | 1.69 |
| 11-06 12:46 | +15 | SOL | DOWN | 0.56 | 0.71 | 1.17 |
| 11-06 12:46 | +10 | SOL | DOWN | 0.56 | 0.66 | 0.66 |
| 11-06 12:46 | +5 | SOL | DOWN | 0.55 | 0.62 | 0.35 |
| 11-06 12:46 | +10 stop | XRP | DOWN | 0.58 | 0.70 | 0.87 |
| 11-06 12:46 | +20 | XRP | DOWN | 0.58 | 0.80 | 1.90 |
| 11-06 12:46 | +15 | XRP | DOWN | 0.58 | 0.80 | 1.90 |
| 11-06 12:46 | +10 | XRP | DOWN | 0.58 | 0.70 | 0.87 |
| 11-06 12:46 | +5 | XRP | DOWN | 0.58 | 0.66 | 0.46 |
| 11-06 12:46 | +10 stop | NEAR | DOWN | 0.64 | 0.74 | 0.69 |
| 11-06 12:46 | +20 | NEAR | DOWN | 0.64 | 0.90 | 2.37 |
| 11-06 12:46 | +15 | NEAR | DOWN | 0.64 | 0.83 | 1.63 |
| 11-06 12:46 | +10 | NEAR | DOWN | 0.64 | 0.74 | 0.69 |
| 11-06 12:46 | +5 | NEAR | DOWN | 0.64 | 0.74 | 0.69 |
| 11-06 12:46 | +10 stop | DOGE | DOWN | 0.53 | 0.64 | 0.75 |
| 11-06 12:46 | +20 | DOGE | DOWN | 0.53 | 0.75 | 1.88 |
| 11-06 12:46 | +15 | DOGE | DOWN | 0.55 | 0.75 | 1.68 |
| 11-06 12:46 | +10 | DOGE | DOWN | 0.55 | 0.66 | 0.76 |
| 11-06 12:46 | +5 | DOGE | DOWN | 0.55 | 0.64 | 0.55 |
| 11-06 12:46 | +10 stop | ETH | DOWN | 0.59 | 0.79 | 1.71 |
| 11-06 12:46 | +20 | ETH | DOWN | 0.59 | 0.79 | 1.71 |
| 11-06 12:46 | +15 | ETH | DOWN | 0.59 | 0.79 | 1.71 |
