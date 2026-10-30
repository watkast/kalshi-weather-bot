# Range-Scalp Bot

*Updated Fri Oct 30 09:22 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 40543 | 35393 | 5150 (51) | 6 | $-11278.47 | -4.4% |
| **+10¢** | 30206 | 24249 | 5957 (74) | 7 | $-10042.50 | -5.3% |
| **+15¢** | 25255 | 18842 | 6413 (101) | 7 | $-9066.29 | -5.7% |
| **+20¢** | 22417 | 15696 | 6721 (130) | 7 | $-7978.93 | -5.7% |
| **+10¢ (15¢ stop)** | 49450 | 49380 | 70 (37) | 3 | $-18743.26 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-30 09:21 | +10 stop | ZEC | DOWN | 0.64 | open |  |
| 10-30 09:20 | +5 | SOL | DOWN | 0.63 | 0.71 | 0.48 |
| 10-30 09:19 | +10 stop | XRP | UP | 0.64 | 0.44 | -2.35 |
| 10-30 09:19 | +20 | XRP | UP | 0.64 | open |  |
| 10-30 09:19 | +15 | XRP | UP | 0.64 | open |  |
| 10-30 09:19 | +10 | XRP | UP | 0.64 | open |  |
| 10-30 09:19 | +5 | XRP | UP | 0.64 | open |  |
| 10-30 09:19 | +10 stop | NEAR | DOWN | 0.56 | 0.68 | 0.86 |
| 10-30 09:19 | +10 stop | SOL | DOWN | 0.63 | 0.74 | 0.79 |
| 10-30 09:19 | +10 stop | DOGE | UP | 0.58 | 0.32 | -2.94 |
| 10-30 09:19 | +10 | DOGE | UP | 0.58 | open |  |
| 10-30 09:19 | +5 | DOGE | UP | 0.58 | open |  |
| 10-30 09:19 | +5 | ZEC | UP | 0.67 | open |  |
| 10-30 09:19 | +10 stop | BNB | UP | 0.53 | open |  |
| 10-30 09:19 | +5 | ETH | UP | 0.58 | open |  |
| 10-30 09:18 | +10 stop | BTC | DOWN | 0.59 | 0.69 | 0.68 |
| 10-30 09:17 | +10 stop | SOL | DOWN | 0.62 | 0.45 | -2.05 |
| 10-30 09:17 | +20 | SOL | DOWN | 0.62 | 0.83 | 1.83 |
| 10-30 09:17 | +15 | SOL | DOWN | 0.62 | 0.83 | 1.83 |
| 10-30 09:17 | +10 | SOL | DOWN | 0.63 | 0.74 | 0.79 |
| 10-30 09:17 | +5 | SOL | DOWN | 0.63 | 0.69 | 0.28 |
| 10-30 09:17 | +10 stop | HYPE | DOWN | 0.63 | 0.74 | 0.79 |
| 10-30 09:17 | +20 | HYPE | DOWN | 0.63 | 0.84 | 1.83 |
| 10-30 09:17 | +15 | HYPE | DOWN | 0.63 | 0.80 | 1.41 |
| 10-30 09:17 | +10 | HYPE | DOWN | 0.63 | 0.74 | 0.79 |
| 10-30 09:17 | +5 | HYPE | DOWN | 0.63 | 0.74 | 0.79 |
| 10-30 09:17 | +5 | DOGE | UP | 0.56 | 0.67 | 0.76 |
| 10-30 09:16 | +10 stop | ETH | UP | 0.56 | open |  |
| 10-30 09:16 | +20 | ETH | UP | 0.56 | open |  |
| 10-30 09:16 | +15 | ETH | UP | 0.56 | open |  |
| 10-30 09:16 | +10 | ETH | UP | 0.56 | open |  |
| 10-30 09:16 | +5 | ETH | UP | 0.56 | 0.61 | 0.15 |
| 10-30 09:16 | +10 stop | NEAR | DOWN | 0.63 | 0.44 | -2.25 |
| 10-30 09:16 | +20 | NEAR | DOWN | 0.63 | open |  |
| 10-30 09:16 | +15 | NEAR | DOWN | 0.63 | open |  |
| 10-30 09:16 | +10 | NEAR | DOWN | 0.63 | open |  |
| 10-30 09:16 | +5 | NEAR | DOWN | 0.63 | 0.68 | 0.17 |
| 10-30 09:16 | +10 stop | BNB | UP | 0.71 | 0.54 | -2.03 |
| 10-30 09:16 | +20 | BNB | UP | 0.71 | open |  |
| 10-30 09:16 | +10 stop | BTC | UP | 0.62 | 0.41 | -2.44 |
