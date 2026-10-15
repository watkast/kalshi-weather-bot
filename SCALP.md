# Range-Scalp Bot

*Updated Thu Oct 15 21:16 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 18167 | 15770 | 2397 (28) | 3 | $-5579.61 | -4.9% |
| **+10¢** | 13721 | 10945 | 2776 (40) | 4 | $-5058.96 | -5.9% |
| **+15¢** | 11505 | 8517 | 2988 (59) | 4 | $-4590.07 | -6.4% |
| **+20¢** | 10221 | 7099 | 3122 (77) | 4 | $-3985.52 | -6.2% |
| **+10¢ (15¢ stop)** | 22353 | 22303 | 50 (29) | 4 | $-8646.48 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 21:16 | +10 stop | HYPE | UP | 0.61 | open |  |
| 10-15 21:16 | +20 | HYPE | UP | 0.61 | open |  |
| 10-15 21:16 | +15 | HYPE | UP | 0.60 | open |  |
| 10-15 21:16 | +10 | HYPE | UP | 0.60 | open |  |
| 10-15 21:16 | +5 | HYPE | UP | 0.61 | open |  |
| 10-15 21:16 | +10 stop | SOL | UP | 0.57 | open |  |
| 10-15 21:16 | +20 | SOL | UP | 0.57 | open |  |
| 10-15 21:16 | +15 | SOL | UP | 0.57 | open |  |
| 10-15 21:16 | +10 | SOL | UP | 0.57 | open |  |
| 10-15 21:16 | +5 | SOL | UP | 0.57 | 0.64 | 0.35 |
| 10-15 21:16 | +10 stop | DOGE | UP | 0.57 | open |  |
| 10-15 21:16 | +20 | DOGE | UP | 0.56 | open |  |
| 10-15 21:16 | +15 | DOGE | UP | 0.56 | open |  |
| 10-15 21:16 | +10 | DOGE | UP | 0.56 | open |  |
| 10-15 21:16 | +5 | DOGE | UP | 0.56 | open |  |
| 10-15 21:16 | +10 stop | ZEC | UP | 0.55 | open |  |
| 10-15 21:16 | +20 | ZEC | UP | 0.55 | open |  |
| 10-15 21:16 | +15 | ZEC | UP | 0.55 | open |  |
| 10-15 21:16 | +10 | ZEC | UP | 0.55 | open |  |
| 10-15 21:16 | +5 | ZEC | UP | 0.55 | open |  |
| 10-15 21:13 | +10 stop | DOGE | DOWN | 0.51 | 0.61 | 0.69 |
| 10-15 21:13 | +10 | DOGE | DOWN | 0.51 | 0.61 | 0.69 |
| 10-15 21:13 | +5 | DOGE | DOWN | 0.51 | 0.61 | 0.70 |
| 10-15 21:11 | +10 stop | XRP | DOWN | 0.59 | 0.37 | -2.54 |
| 10-15 21:10 | +5 | DOGE | UP | 0.71 | 0.82 | 0.84 |
| 10-15 21:10 | +5 | XRP | DOWN | 0.66 | 0.72 | 0.29 |
| 10-15 21:10 | +10 stop | BNB | DOWN | 0.65 | 0.76 | 0.84 |
| 10-15 21:10 | +10 | BNB | DOWN | 0.65 | 0.76 | 0.84 |
| 10-15 21:10 | +5 | BNB | DOWN | 0.65 | 0.70 | 0.22 |
| 10-15 21:10 | +10 stop | DOGE | UP | 0.71 | 0.82 | 0.88 |
| 10-15 21:10 | +10 stop | HYPE | DOWN | 0.40 | 0.54 | 1.05 |
| 10-15 21:10 | +15 | HYPE | DOWN | 0.40 | yes | -4.17 |
| 10-15 21:10 | +10 | HYPE | DOWN | 0.40 | 0.54 | 1.05 |
| 10-15 21:10 | +5 | HYPE | DOWN | 0.40 | 0.54 | 1.05 |
| 10-15 21:09 | +10 stop | DOGE | UP | 0.58 | 0.43 | -1.86 |
| 10-15 21:09 | +10 | DOGE | UP | 0.58 | 0.69 | 0.77 |
| 10-15 21:09 | +5 | DOGE | UP | 0.58 | 0.64 | 0.25 |
| 10-15 21:09 | +10 stop | HYPE | DOWN | 0.36 | 0.68 | 2.87 |
| 10-15 21:08 | +10 stop | XRP | DOWN | 0.69 | 0.52 | -2.03 |
| 10-15 21:08 | +10 | XRP | DOWN | 0.69 | 0.93 | 2.16 |
