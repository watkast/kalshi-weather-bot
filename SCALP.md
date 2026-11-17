# Range-Scalp Bot

*Updated Tue Nov 17 04:54 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 62595 | 54604 | 7991 (117) | 6 | $-16997.89 | -4.3% |
| **+10¢** | 46749 | 37400 | 9349 (159) | 5 | $-15862.85 | -5.4% |
| **+15¢** | 39181 | 29098 | 10083 (201) | 6 | $-14412.48 | -5.9% |
| **+20¢** | 34923 | 24350 | 10573 (256) | 7 | $-12580.48 | -5.7% |
| **+10¢ (15¢ stop)** | 76186 | 76030 | 156 (92) | 4 | $-28078.43 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-17 04:54 | +10 stop | DOGE | DOWN | 0.65 | open |  |
| 11-17 04:54 | +10 stop | XRP | DOWN | 0.68 | open |  |
| 11-17 04:54 | +20 | XRP | DOWN | 0.69 | open |  |
| 11-17 04:54 | +15 | XRP | DOWN | 0.67 | open |  |
| 11-17 04:54 | +10 | XRP | DOWN | 0.67 | open |  |
| 11-17 04:53 | +10 stop | HYPE | UP | 0.62 | open |  |
| 11-17 04:53 | +10 stop | BTC | DOWN | 0.66 | open |  |
| 11-17 04:53 | +20 | BTC | DOWN | 0.66 | open |  |
| 11-17 04:53 | +15 | BTC | DOWN | 0.66 | open |  |
| 11-17 04:53 | +10 | BTC | DOWN | 0.66 | open |  |
| 11-17 04:53 | +5 | BTC | DOWN | 0.66 | open |  |
| 11-17 04:53 | +10 stop | NEAR | UP | 0.61 | 0.74 | 0.99 |
| 11-17 04:51 | +10 stop | ETH | DOWN | 0.56 | 0.33 | -2.64 |
| 11-17 04:51 | +10 stop | ZEC | UP | 0.64 | 0.76 | 0.90 |
| 11-17 04:51 | +20 | ZEC | UP | 0.64 | open |  |
| 11-17 04:51 | +5 | ZEC | UP | 0.64 | 0.72 | 0.48 |
| 11-17 04:51 | +10 stop | NEAR | DOWN | 0.60 | 0.43 | -2.03 |
| 11-17 04:50 | +10 stop | BNB | DOWN | 0.67 | 0.48 | -2.24 |
| 11-17 04:50 | +10 stop | HYPE | DOWN | 0.69 | 0.40 | -3.22 |
| 11-17 04:50 | +10 | HYPE | DOWN | 0.69 | open |  |
| 11-17 04:50 | +15 | ZEC | UP | 0.70 | open |  |
| 11-17 04:50 | +10 | ZEC | UP | 0.70 | 0.80 | 0.73 |
| 11-17 04:50 | +5 | ZEC | UP | 0.70 | 0.77 | 0.42 |
| 11-17 04:50 | +10 stop | XRP | DOWN | 0.69 | 0.80 | 0.83 |
| 11-17 04:50 | +10 stop | NEAR | DOWN | 0.44 | 0.59 | 1.15 |
| 11-17 04:49 | +10 stop | ETH | UP | 0.65 | 0.47 | -2.13 |
| 11-17 04:49 | +15 | BNB | UP | 0.55 | open |  |
| 11-17 04:49 | +10 | BNB | UP | 0.55 | open |  |
| 11-17 04:49 | +5 | BNB | UP | 0.55 | open |  |
| 11-17 04:49 | +10 | ETH | UP | 0.70 | 0.84 | 1.15 |
| 11-17 04:49 | +10 stop | XRP | UP | 0.58 | 0.40 | -2.15 |
| 11-17 04:49 | +5 | XRP | UP | 0.60 | open |  |
| 11-17 04:49 | +10 stop | BNB | UP | 0.64 | 0.47 | -2.05 |
| 11-17 04:48 | +5 | ETH | UP | 0.69 | 0.76 | 0.42 |
| 11-17 04:48 | +10 stop | SOL | UP | 0.46 | 0.28 | -2.13 |
| 11-17 04:48 | +10 stop | ETH | UP | 0.59 | 0.69 | 0.68 |
| 11-17 04:48 | +5 | ETH | UP | 0.59 | 0.64 | 0.16 |
| 11-17 04:48 | +10 stop | DOGE | UP | 0.54 | 0.38 | -1.95 |
| 11-17 04:48 | +10 | DOGE | UP | 0.57 | open |  |
| 11-17 04:48 | +5 | ZEC | UP | 0.63 | 0.77 | 1.10 |
