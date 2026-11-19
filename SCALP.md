# Range-Scalp Bot

*Updated Thu Nov 19 02:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 64647 | 56404 | 8243 (124) | 1 | $-17506.42 | -4.3% |
| **+10¢** | 48293 | 38650 | 9643 (165) | 1 | $-16319.20 | -5.4% |
| **+15¢** | 40497 | 30100 | 10397 (210) | 2 | $-14740.33 | -5.8% |
| **+20¢** | 36066 | 25149 | 10917 (265) | 1 | $-13040.82 | -5.8% |
| **+10¢ (15¢ stop)** | 78648 | 78484 | 164 (98) | 0 | $-28882.44 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-19 02:58 | +15 | XRP | DOWN | 0.70 | open |  |
| 11-19 02:58 | +10 | XRP | DOWN | 0.70 | open |  |
| 11-19 02:58 | +5 | XRP | DOWN | 0.67 | open |  |
| 11-19 02:57 | +10 stop | SOL | UP | 0.31 | 0.56 | 2.17 |
| 11-19 02:57 | +10 stop | ETH | UP | 0.36 | 0.63 | 2.36 |
| 11-19 02:57 | +20 | ETH | UP | 0.39 | 0.63 | 2.06 |
| 11-19 02:57 | +15 | ETH | UP | 0.41 | 0.63 | 1.86 |
| 11-19 02:57 | +10 | ETH | UP | 0.44 | 0.63 | 1.55 |
| 11-19 02:56 | +10 stop | BTC | DOWN | 0.70 | 0.88 | 1.57 |
| 11-19 02:56 | +10 | BTC | DOWN | 0.70 | 0.88 | 1.57 |
| 11-19 02:56 | +5 | BTC | DOWN | 0.70 | 0.88 | 1.57 |
| 11-19 02:56 | +10 stop | DOGE | UP | 0.45 | 0.60 | 1.15 |
| 11-19 02:53 | +15 | XRP | UP | 0.70 | 0.88 | 1.57 |
| 11-19 02:53 | +5 | XRP | UP | 0.70 | 0.76 | 0.32 |
| 11-19 02:53 | +10 stop | ZEC | DOWN | 0.58 | 0.43 | -1.86 |
| 11-19 02:53 | +10 | XRP | UP | 0.66 | 0.76 | 0.71 |
| 11-19 02:53 | +5 | XRP | UP | 0.57 | 0.65 | 0.48 |
| 11-19 02:53 | +10 stop | XRP | UP | 0.59 | 0.69 | 0.68 |
| 11-19 02:52 | +20 | DOGE | DOWN | 0.67 | 0.91 | 2.17 |
| 11-19 02:52 | +5 | DOGE | DOWN | 0.67 | 0.91 | 2.17 |
| 11-19 02:52 | +10 stop | ETH | DOWN | 0.59 | 0.35 | -2.73 |
| 11-19 02:52 | +5 | ETH | DOWN | 0.60 | 0.84 | 2.13 |
| 11-19 02:52 | +5 | SOL | DOWN | 0.69 | 0.84 | 1.25 |
| 11-19 02:51 | +10 stop | NEAR | UP | 0.68 | 0.78 | 0.71 |
| 11-19 02:51 | +20 | NEAR | UP | 0.68 | 0.89 | 1.87 |
| 11-19 02:51 | +15 | NEAR | UP | 0.68 | 0.84 | 1.34 |
| 11-19 02:51 | +5 | ETH | DOWN | 0.49 | 0.61 | 0.85 |
| 11-19 02:51 | +10 stop | XRP | DOWN | 0.49 | 0.60 | 0.75 |
| 11-19 02:51 | +10 stop | BTC | DOWN | 0.55 | 0.38 | -2.05 |
| 11-19 02:51 | +10 stop | ETH | DOWN | 0.68 | 0.49 | -2.24 |
| 11-19 02:51 | +10 stop | BNB | UP | 0.47 | 0.59 | 0.85 |
| 11-19 02:51 | +20 | BNB | UP | 0.47 | 0.75 | 2.48 |
| 11-19 02:51 | +15 | BNB | UP | 0.46 | 0.75 | 2.58 |
| 11-19 02:51 | +10 | BNB | UP | 0.49 | 0.59 | 0.65 |
| 11-19 02:51 | +5 | BNB | UP | 0.50 | 0.59 | 0.55 |
| 11-19 02:49 | +10 stop | BTC | DOWN | 0.50 | 0.64 | 1.05 |
| 11-19 02:49 | +15 | DOGE | DOWN | 0.66 | 0.91 | 2.27 |
| 11-19 02:49 | +5 | DOGE | DOWN | 0.66 | 0.72 | 0.29 |
| 11-19 02:48 | +10 stop | SOL | DOWN | 0.61 | 0.33 | -3.13 |
| 11-19 02:48 | +20 | SOL | DOWN | 0.61 | 0.84 | 2.03 |
