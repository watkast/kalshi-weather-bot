# Range-Scalp Bot

*Updated Wed Oct 21 09:42 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 27000 | 23510 | 3490 (39) | 5 | $-7858.02 | -4.6% |
| **+10¢** | 20313 | 16281 | 4032 (55) | 3 | $-6943.78 | -5.4% |
| **+15¢** | 16999 | 12661 | 4338 (78) | 6 | $-6213.93 | -5.8% |
| **+20¢** | 15053 | 10505 | 4548 (97) | 5 | $-5586.85 | -5.9% |
| **+10¢ (15¢ stop)** | 33119 | 33060 | 59 (32) | 0 | $-12258.68 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 09:42 | +5 | XRP | DOWN | 0.68 | open |  |
| 10-21 09:42 | +10 stop | XRP | DOWN | 0.45 | 0.56 | 0.74 |
| 10-21 09:42 | +5 | XRP | DOWN | 0.45 | 0.53 | 0.44 |
| 10-21 09:42 | +10 stop | BTC | DOWN | 0.54 | 0.69 | 1.17 |
| 10-21 09:41 | +10 stop | BTC | DOWN | 0.66 | 0.41 | -2.83 |
| 10-21 09:41 | +10 | BTC | DOWN | 0.71 | open |  |
| 10-21 09:41 | +5 | BTC | DOWN | 0.71 | open |  |
| 10-21 09:40 | +10 stop | XRP | UP | 0.65 | 0.49 | -1.94 |
| 10-21 09:40 | +20 | XRP | UP | 0.67 | open |  |
| 10-21 09:40 | +15 | XRP | UP | 0.63 | open |  |
| 10-21 09:40 | +10 | XRP | UP | 0.63 | open |  |
| 10-21 09:40 | +5 | XRP | UP | 0.63 | 0.69 | 0.28 |
| 10-21 09:40 | +10 stop | HYPE | DOWN | 0.61 | 0.45 | -1.99 |
| 10-21 09:40 | +5 | HYPE | DOWN | 0.61 | open |  |
| 10-21 09:39 | +10 stop | NEAR | UP | 0.51 | 0.34 | -2.04 |
| 10-21 09:39 | +10 stop | HYPE | UP | 0.52 | 0.35 | -2.04 |
| 10-21 09:39 | +15 | HYPE | UP | 0.52 | 0.88 | 3.34 |
| 10-21 09:39 | +10 | HYPE | UP | 0.52 | 0.88 | 3.34 |
| 10-21 09:39 | +5 | HYPE | UP | 0.52 | 0.60 | 0.45 |
| 10-21 09:38 | +10 stop | BNB | DOWN | 0.61 | 0.73 | 0.84 |
| 10-21 09:38 | +10 | BNB | DOWN | 0.60 | 0.73 | 0.99 |
| 10-21 09:38 | +5 | BNB | DOWN | 0.60 | 0.73 | 0.99 |
| 10-21 09:38 | +10 stop | DOGE | DOWN | 0.69 | 0.79 | 0.73 |
| 10-21 09:38 | +10 | DOGE | DOWN | 0.69 | 0.79 | 0.73 |
| 10-21 09:38 | +5 | DOGE | DOWN | 0.69 | 0.79 | 0.73 |
| 10-21 09:37 | +10 stop | ETH | DOWN | 0.64 | 0.74 | 0.69 |
| 10-21 09:37 | +20 | ETH | DOWN | 0.64 | 0.86 | 1.94 |
| 10-21 09:37 | +10 stop | BTC | DOWN | 0.62 | 0.74 | 0.89 |
| 10-21 09:37 | +10 | BTC | DOWN | 0.62 | 0.74 | 0.89 |
| 10-21 09:37 | +5 | BTC | DOWN | 0.62 | 0.68 | 0.27 |
| 10-21 09:37 | +10 stop | DOGE | UP | 0.41 | 0.54 | 0.95 |
| 10-21 09:37 | +10 stop | BNB | UP | 0.48 | 0.62 | 1.05 |
| 10-21 09:37 | +20 | BNB | UP | 0.48 | open |  |
| 10-21 09:37 | +15 | BNB | UP | 0.48 | open |  |
| 10-21 09:37 | +10 | BNB | UP | 0.48 | 0.62 | 1.05 |
| 10-21 09:37 | +5 | BNB | UP | 0.48 | 0.62 | 1.05 |
| 10-21 09:37 | +20 | DOGE | UP | 0.43 | open |  |
| 10-21 09:37 | +15 | DOGE | UP | 0.43 | open |  |
| 10-21 09:37 | +10 | DOGE | UP | 0.43 | 0.54 | 0.74 |
| 10-21 09:37 | +5 | DOGE | UP | 0.43 | 0.54 | 0.74 |
