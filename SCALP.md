# Range-Scalp Bot

*Updated Thu Oct 29 23:07 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 39861 | 34815 | 5046 (51) | 1 | $-10947.62 | -4.4% |
| **+10¢** | 29709 | 23873 | 5836 (74) | 1 | $-9683.56 | -5.2% |
| **+15¢** | 24844 | 18565 | 6279 (101) | 1 | $-8682.24 | -5.6% |
| **+20¢** | 22045 | 15461 | 6584 (130) | 1 | $-7604.64 | -5.5% |
| **+10¢ (15¢ stop)** | 48657 | 48587 | 70 (37) | 0 | $-18379.78 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-29 23:02 | +10 stop | BNB | DOWN | 0.55 | 0.65 | 0.66 |
| 10-29 23:01 | +10 | SOL | DOWN | 0.70 | 0.81 | 0.84 |
| 10-29 23:01 | +5 | SOL | DOWN | 0.70 | 0.77 | 0.42 |
| 10-29 23:01 | +10 stop | BTC | DOWN | 0.61 | 0.75 | 1.09 |
| 10-29 23:01 | +20 | BTC | DOWN | 0.61 | 0.81 | 1.72 |
| 10-29 23:01 | +15 | BTC | DOWN | 0.61 | 0.80 | 1.61 |
| 10-29 23:01 | +10 | BTC | DOWN | 0.61 | 0.75 | 1.09 |
| 10-29 23:01 | +5 | BTC | DOWN | 0.61 | 0.69 | 0.48 |
| 10-29 23:01 | +10 stop | NEAR | DOWN | 0.66 | 0.79 | 1.02 |
| 10-29 23:01 | +20 | NEAR | DOWN | 0.65 | 0.85 | 1.75 |
| 10-29 23:01 | +15 | NEAR | DOWN | 0.65 | 0.80 | 1.22 |
| 10-29 23:01 | +10 | NEAR | DOWN | 0.65 | 0.79 | 1.12 |
| 10-29 23:01 | +5 | NEAR | DOWN | 0.65 | 0.79 | 1.12 |
| 10-29 23:01 | +10 stop | ZEC | DOWN | 0.69 | 0.82 | 1.04 |
| 10-29 23:01 | +20 | ZEC | DOWN | 0.69 | 0.91 | 2.00 |
| 10-29 23:01 | +15 | ZEC | DOWN | 0.69 | 0.86 | 1.46 |
| 10-29 23:01 | +10 | ZEC | DOWN | 0.69 | 0.82 | 1.04 |
| 10-29 23:01 | +5 | ZEC | DOWN | 0.69 | 0.74 | 0.21 |
| 10-29 23:01 | +10 stop | BNB | UP | 0.58 | 0.41 | -2.05 |
| 10-29 23:01 | +20 | BNB | UP | 0.57 | open |  |
| 10-29 23:01 | +15 | BNB | UP | 0.57 | open |  |
| 10-29 23:01 | +10 | BNB | UP | 0.57 | open |  |
| 10-29 23:01 | +5 | BNB | UP | 0.57 | open |  |
| 10-29 23:00 | +10 stop | ETH | DOWN | 0.61 | 0.71 | 0.68 |
| 10-29 23:00 | +20 | ETH | DOWN | 0.60 | 0.80 | 1.71 |
| 10-29 23:00 | +15 | ETH | DOWN | 0.60 | 0.79 | 1.61 |
| 10-29 23:00 | +10 | ETH | DOWN | 0.60 | 0.71 | 0.78 |
| 10-29 23:00 | +5 | ETH | DOWN | 0.61 | 0.66 | 0.17 |
| 10-29 22:56 | +10 stop | ETH | DOWN | 0.63 | 0.78 | 1.20 |
| 10-29 22:56 | +10 | ETH | DOWN | 0.63 | 0.78 | 1.20 |
| 10-29 22:56 | +5 | ETH | DOWN | 0.63 | 0.78 | 1.20 |
| 10-29 22:56 | +5 | BNB | UP | 0.70 | 0.90 | 1.79 |
| 10-29 22:55 | +10 stop | BTC | DOWN | 0.70 | 0.83 | 1.05 |
| 10-29 22:55 | +15 | BTC | DOWN | 0.70 | 0.91 | 1.91 |
| 10-29 22:55 | +10 | BTC | DOWN | 0.70 | 0.83 | 1.05 |
| 10-29 22:55 | +5 | BTC | DOWN | 0.70 | 0.83 | 1.05 |
| 10-29 22:53 | +5 | ETH | DOWN | 0.71 | 0.76 | 0.22 |
| 10-29 22:52 | +5 | BTC | DOWN | 0.63 | 0.72 | 0.58 |
| 10-29 22:52 | +10 stop | ETH | DOWN | 0.53 | 0.69 | 1.27 |
| 10-29 22:52 | +5 | ETH | DOWN | 0.53 | 0.58 | 0.14 |
