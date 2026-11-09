# Range-Scalp Bot

*Updated Mon Nov 09 05:16 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 53342 | 46506 | 6836 (85) | 1 | $-14764.19 | -4.4% |
| **+10¢** | 39841 | 31867 | 7974 (110) | 1 | $-13771.87 | -5.5% |
| **+15¢** | 33385 | 24793 | 8592 (141) | 1 | $-12577.96 | -6.0% |
| **+20¢** | 29706 | 20698 | 9008 (186) | 1 | $-11069.53 | -5.9% |
| **+10¢ (15¢ stop)** | 65007 | 64901 | 106 (63) | 1 | $-24139.62 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-09 05:15 | +10 stop | ZEC | DOWN | 0.66 | open |  |
| 11-09 05:15 | +20 | ZEC | DOWN | 0.66 | open |  |
| 11-09 05:15 | +15 | ZEC | DOWN | 0.66 | open |  |
| 11-09 05:15 | +10 | ZEC | DOWN | 0.66 | open |  |
| 11-09 05:15 | +5 | ZEC | DOWN | 0.66 | open |  |
| 11-09 05:12 | +10 stop | DOGE | UP | 0.49 | 0.13 | -3.86 |
| 11-09 05:12 | +20 | DOGE | UP | 0.49 | no | -5.08 |
| 11-09 05:12 | +15 | DOGE | UP | 0.49 | no | -5.08 |
| 11-09 05:12 | +10 | DOGE | UP | 0.49 | no | -5.08 |
| 11-09 05:12 | +5 | DOGE | UP | 0.49 | 0.55 | 0.24 |
| 11-09 05:12 | +10 stop | HYPE | UP | 0.46 | 0.56 | 0.67 |
| 11-09 05:12 | +20 | HYPE | UP | 0.46 | no | -4.75 |
| 11-09 05:12 | +15 | HYPE | UP | 0.43 | no | -4.48 |
| 11-09 05:12 | +10 | HYPE | UP | 0.43 | 0.56 | 0.94 |
| 11-09 05:12 | +5 | HYPE | UP | 0.43 | 0.56 | 0.94 |
| 11-09 05:12 | +10 stop | ETH | UP | 0.61 | 0.46 | -1.85 |
| 11-09 05:12 | +20 | ETH | UP | 0.57 | 0.96 | 3.70 |
| 11-09 05:12 | +15 | ETH | UP | 0.57 | 0.96 | 3.70 |
| 11-09 05:12 | +10 | ETH | UP | 0.56 | 0.67 | 0.76 |
| 11-09 05:12 | +5 | ETH | UP | 0.59 | 0.67 | 0.47 |
| 11-09 05:11 | +10 stop | XRP | UP | 0.51 | 0.73 | 1.88 |
| 11-09 05:11 | +10 stop | BNB | DOWN | 0.65 | 0.39 | -2.97 |
| 11-09 05:11 | +20 | BNB | DOWN | 0.65 | yes | -6.64 |
| 11-09 05:11 | +15 | BNB | DOWN | 0.65 | yes | -6.66 |
| 11-09 05:11 | +10 | BNB | DOWN | 0.66 | yes | -6.76 |
| 11-09 05:11 | +5 | BNB | DOWN | 0.66 | yes | -6.80 |
| 11-09 05:11 | +10 stop | ZEC | UP | 0.59 | 0.69 | 0.68 |
| 11-09 05:09 | +10 stop | XRP | DOWN | 0.64 | 0.41 | -2.59 |
| 11-09 05:09 | +10 | XRP | DOWN | 0.63 | yes | -6.47 |
| 11-09 05:09 | +5 | XRP | DOWN | 0.63 | yes | -6.47 |
| 11-09 05:07 | +10 stop | ZEC | DOWN | 0.71 | 0.46 | -2.83 |
| 11-09 05:07 | +10 stop | XRP | DOWN | 0.65 | 0.77 | 0.91 |
| 11-09 05:07 | +10 stop | BNB | DOWN | 0.64 | 0.91 | 2.46 |
| 11-09 05:06 | +5 | DOGE | DOWN | 0.66 | 0.78 | 0.91 |
| 11-09 05:06 | +10 stop | SOL | DOWN | 0.71 | 0.85 | 1.16 |
| 11-09 05:06 | +10 | SOL | DOWN | 0.71 | 0.85 | 1.16 |
| 11-09 05:06 | +5 | SOL | DOWN | 0.71 | 0.78 | 0.42 |
| 11-09 05:06 | +10 stop | DOGE | DOWN | 0.68 | 0.78 | 0.71 |
| 11-09 05:06 | +10 stop | HYPE | DOWN | 0.67 | 0.80 | 1.02 |
| 11-09 05:06 | +10 stop | DOGE | UP | 0.39 | 0.56 | 1.35 |
