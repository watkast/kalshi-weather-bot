# Range-Scalp Bot

*Updated Sat Oct 24 05:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 31494 | 27451 | 4043 (40) | 1 | $-9054.85 | -4.6% |
| **+10¢** | 23555 | 18886 | 4669 (58) | 1 | $-8035.25 | -5.4% |
| **+15¢** | 19721 | 14703 | 5018 (81) | 2 | $-7162.96 | -5.8% |
| **+20¢** | 17473 | 12218 | 5255 (103) | 2 | $-6366.80 | -5.8% |
| **+10¢ (15¢ stop)** | 38651 | 38592 | 59 (32) | 0 | $-14759.18 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-24 05:19 | +10 stop | BNB | DOWN | 0.61 | 0.83 | 1.93 |
| 10-24 05:19 | +10 | BNB | DOWN | 0.61 | 0.83 | 1.93 |
| 10-24 05:19 | +5 | BNB | DOWN | 0.61 | 0.69 | 0.48 |
| 10-24 05:19 | +10 stop | BTC | DOWN | 0.60 | 0.70 | 0.68 |
| 10-24 05:18 | +10 stop | DOGE | DOWN | 0.69 | 0.83 | 1.15 |
| 10-24 05:18 | +10 | DOGE | DOWN | 0.69 | 0.83 | 1.15 |
| 10-24 05:18 | +5 | DOGE | DOWN | 0.69 | 0.76 | 0.42 |
| 10-24 05:18 | +5 | ETH | DOWN | 0.58 | 0.63 | 0.15 |
| 10-24 05:17 | +5 | ZEC | DOWN | 0.70 | 0.79 | 0.63 |
| 10-24 05:17 | +10 stop | DOGE | UP | 0.49 | 0.59 | 0.65 |
| 10-24 05:17 | +20 | DOGE | UP | 0.49 | open |  |
| 10-24 05:17 | +15 | DOGE | UP | 0.49 | open |  |
| 10-24 05:17 | +10 | DOGE | UP | 0.49 | 0.59 | 0.65 |
| 10-24 05:17 | +5 | DOGE | UP | 0.49 | 0.59 | 0.65 |
| 10-24 05:17 | +10 stop | ETH | DOWN | 0.55 | 0.69 | 1.07 |
| 10-24 05:17 | +20 | ETH | DOWN | 0.55 | 0.76 | 1.79 |
| 10-24 05:17 | +15 | ETH | DOWN | 0.55 | 0.71 | 1.27 |
| 10-24 05:17 | +10 | ETH | DOWN | 0.55 | 0.69 | 1.07 |
| 10-24 05:17 | +5 | ETH | DOWN | 0.55 | 0.61 | 0.25 |
| 10-24 05:16 | +10 stop | BTC | UP | 0.60 | 0.35 | -2.83 |
| 10-24 05:16 | +20 | BTC | UP | 0.60 | open |  |
| 10-24 05:16 | +15 | BTC | UP | 0.60 | open |  |
| 10-24 05:16 | +10 | BTC | UP | 0.60 | open |  |
| 10-24 05:16 | +5 | BTC | UP | 0.60 | open |  |
| 10-24 05:16 | +10 stop | HYPE | DOWN | 0.64 | 0.84 | 1.73 |
| 10-24 05:16 | +20 | HYPE | DOWN | 0.64 | 0.84 | 1.73 |
| 10-24 05:16 | +15 | HYPE | DOWN | 0.64 | 0.84 | 1.73 |
| 10-24 05:16 | +10 | HYPE | DOWN | 0.64 | 0.84 | 1.73 |
| 10-24 05:16 | +5 | HYPE | DOWN | 0.64 | 0.84 | 1.73 |
| 10-24 05:16 | +10 stop | BNB | DOWN | 0.56 | 0.68 | 0.86 |
| 10-24 05:16 | +20 | BNB | DOWN | 0.56 | 0.83 | 2.42 |
| 10-24 05:16 | +15 | BNB | DOWN | 0.56 | 0.83 | 2.42 |
| 10-24 05:16 | +10 | BNB | DOWN | 0.56 | 0.68 | 0.86 |
| 10-24 05:16 | +5 | BNB | DOWN | 0.56 | 0.68 | 0.86 |
| 10-24 05:16 | +10 stop | ZEC | DOWN | 0.58 | 0.68 | 0.66 |
| 10-24 05:16 | +20 | ZEC | DOWN | 0.58 | 0.79 | 1.80 |
| 10-24 05:16 | +15 | ZEC | DOWN | 0.58 | 0.74 | 1.28 |
| 10-24 05:16 | +10 | ZEC | DOWN | 0.58 | 0.68 | 0.66 |
| 10-24 05:16 | +5 | ZEC | DOWN | 0.58 | 0.63 | 0.15 |
| 10-24 05:16 | +10 stop | XRP | DOWN | 0.60 | 0.74 | 1.09 |
