# Range-Scalp Bot

*Updated Mon Nov 16 09:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 61833 | 53943 | 7890 (115) | 4 | $-16741.74 | -4.3% |
| **+10¢** | 46192 | 36953 | 9239 (157) | 4 | $-15647.29 | -5.4% |
| **+15¢** | 38709 | 28745 | 9964 (196) | 4 | $-14260.21 | -5.9% |
| **+20¢** | 34511 | 24062 | 10449 (249) | 4 | $-12461.46 | -5.8% |
| **+10¢ (15¢ stop)** | 75280 | 75126 | 154 (90) | 2 | $-27764.60 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-16 09:42 | +10 stop | BTC | DOWN | 0.56 | open |  |
| 11-16 09:42 | +5 | BTC | DOWN | 0.56 | open |  |
| 11-16 09:41 | +10 stop | BNB | DOWN | 0.63 | 0.46 | -2.05 |
| 11-16 09:41 | +20 | BNB | DOWN | 0.63 | open |  |
| 11-16 09:41 | +15 | BNB | DOWN | 0.63 | open |  |
| 11-16 09:41 | +10 | BNB | DOWN | 0.63 | open |  |
| 11-16 09:41 | +5 | BNB | DOWN | 0.63 | open |  |
| 11-16 09:41 | +10 stop | XRP | UP | 0.68 | open |  |
| 11-16 09:41 | +10 stop | XRP | DOWN | 0.35 | 0.60 | 2.17 |
| 11-16 09:40 | +10 stop | SOL | DOWN | 0.61 | 0.40 | -2.44 |
| 11-16 09:40 | +10 | SOL | DOWN | 0.61 | open |  |
| 11-16 09:40 | +5 | SOL | DOWN | 0.65 | open |  |
| 11-16 09:40 | +10 stop | NEAR | UP | 0.67 | 0.89 | 1.97 |
| 11-16 09:40 | +5 | NEAR | UP | 0.60 | 0.65 | 0.17 |
| 11-16 09:40 | +10 stop | XRP | DOWN | 0.68 | 0.53 | -1.84 |
| 11-16 09:40 | +10 | XRP | DOWN | 0.68 | open |  |
| 11-16 09:40 | +5 | XRP | DOWN | 0.68 | open |  |
| 11-16 09:39 | +10 stop | SOL | UP | 0.65 | 0.30 | -3.81 |
| 11-16 09:39 | +10 stop | BTC | UP | 0.49 | 0.60 | 0.75 |
| 11-16 09:39 | +5 | BTC | UP | 0.49 | 0.60 | 0.75 |
| 11-16 09:38 | +5 | XRP | UP | 0.70 | 0.79 | 0.63 |
| 11-16 09:38 | +5 | ETH | DOWN | 0.61 | 0.74 | 0.99 |
| 11-16 09:38 | +10 stop | ETH | DOWN | 0.55 | 0.65 | 0.66 |
| 11-16 09:38 | +10 stop | NEAR | UP | 0.71 | 0.54 | -2.03 |
| 11-16 09:38 | +15 | NEAR | UP | 0.71 | 0.89 | 1.58 |
| 11-16 09:38 | +10 | NEAR | UP | 0.71 | 0.89 | 1.58 |
| 11-16 09:37 | +10 stop | SOL | UP | 0.55 | 0.65 | 0.66 |
| 11-16 09:37 | +10 stop | ZEC | DOWN | 0.70 | 0.90 | 1.82 |
| 11-16 09:37 | +5 | BTC | UP | 0.57 | 0.63 | 0.25 |
| 11-16 09:37 | +10 stop | BNB | UP | 0.59 | 0.27 | -3.51 |
| 11-16 09:37 | +10 stop | XRP | UP | 0.56 | 0.68 | 0.86 |
| 11-16 09:37 | +10 | XRP | UP | 0.56 | 0.68 | 0.86 |
| 11-16 09:37 | +5 | XRP | UP | 0.56 | 0.63 | 0.35 |
| 11-16 09:36 | +10 stop | ETH | UP | 0.65 | 0.49 | -1.94 |
| 11-16 09:35 | +10 stop | ZEC | UP | 0.60 | 0.40 | -2.34 |
| 11-16 09:35 | +10 stop | DOGE | UP | 0.58 | 0.34 | -2.74 |
| 11-16 09:34 | +10 stop | SOL | UP | 0.69 | 0.79 | 0.73 |
| 11-16 09:34 | +10 stop | BTC | UP | 0.69 | 0.50 | -2.23 |
| 11-16 09:34 | +10 stop | BNB | UP | 0.68 | 0.79 | 0.82 |
| 11-16 09:34 | +10 stop | ETH | DOWN | 0.48 | 0.32 | -1.94 |
