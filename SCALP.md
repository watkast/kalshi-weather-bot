# Range-Scalp Bot

*Updated Thu Oct 29 23:47 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 39902 | 34851 | 5051 (51) | 2 | $-10958.25 | -4.4% |
| **+10¢** | 29738 | 23896 | 5842 (74) | 3 | $-9696.15 | -5.2% |
| **+15¢** | 24866 | 18582 | 6284 (101) | 3 | $-8685.62 | -5.6% |
| **+20¢** | 22065 | 15475 | 6590 (130) | 3 | $-7610.89 | -5.5% |
| **+10¢ (15¢ stop)** | 48706 | 48636 | 70 (37) | 3 | $-18409.10 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-29 23:47 | +5 | BNB | DOWN | 0.70 | open |  |
| 10-29 23:47 | +5 | BNB | DOWN | 0.60 | 0.66 | 0.28 |
| 10-29 23:46 | +10 stop | ZEC | DOWN | 0.68 | open |  |
| 10-29 23:46 | +20 | ZEC | DOWN | 0.69 | open |  |
| 10-29 23:46 | +15 | ZEC | DOWN | 0.70 | open |  |
| 10-29 23:46 | +10 | ZEC | DOWN | 0.70 | open |  |
| 10-29 23:46 | +5 | ZEC | DOWN | 0.70 | open |  |
| 10-29 23:46 | +10 stop | NEAR | DOWN | 0.67 | open |  |
| 10-29 23:46 | +20 | NEAR | DOWN | 0.67 | open |  |
| 10-29 23:46 | +15 | NEAR | DOWN | 0.67 | open |  |
| 10-29 23:46 | +10 | NEAR | DOWN | 0.67 | open |  |
| 10-29 23:46 | +5 | NEAR | DOWN | 0.67 | 0.72 | 0.19 |
| 10-29 23:46 | +10 stop | BNB | DOWN | 0.62 | open |  |
| 10-29 23:46 | +20 | BNB | DOWN | 0.62 | open |  |
| 10-29 23:46 | +15 | BNB | DOWN | 0.62 | open |  |
| 10-29 23:46 | +10 | BNB | DOWN | 0.62 | open |  |
| 10-29 23:46 | +5 | BNB | DOWN | 0.62 | 0.67 | 0.17 |
| 10-29 23:36 | +10 stop | XRP | DOWN | 0.64 | 0.78 | 1.15 |
| 10-29 23:36 | +10 stop | SOL | DOWN | 0.64 | 0.77 | 1.00 |
| 10-29 23:36 | +10 stop | BNB | DOWN | 0.64 | 0.74 | 0.69 |
| 10-29 23:36 | +10 stop | HYPE | DOWN | 0.64 | 0.77 | 1.00 |
| 10-29 23:36 | +5 | XRP | DOWN | 0.59 | 0.64 | 0.16 |
| 10-29 23:35 | +10 | ZEC | DOWN | 0.65 | 0.75 | 0.70 |
| 10-29 23:35 | +10 stop | XRP | UP | 0.56 | 0.36 | -2.35 |
| 10-29 23:35 | +10 | XRP | UP | 0.57 | no | -5.88 |
| 10-29 23:35 | +5 | XRP | UP | 0.57 | 0.62 | 0.15 |
| 10-29 23:34 | +10 stop | ZEC | DOWN | 0.69 | 0.80 | 0.84 |
| 10-29 23:34 | +5 | NEAR | DOWN | 0.60 | 0.68 | 0.47 |
| 10-29 23:34 | +10 stop | ETH | UP | 0.54 | 0.32 | -2.54 |
| 10-29 23:34 | +10 stop | BTC | UP | 0.57 | 0.42 | -1.86 |
| 10-29 23:34 | +10 stop | DOGE | DOWN | 0.71 | 0.82 | 0.84 |
| 10-29 23:34 | +10 | DOGE | DOWN | 0.71 | 0.82 | 0.87 |
| 10-29 23:34 | +5 | DOGE | DOWN | 0.71 | 0.80 | 0.63 |
| 10-29 23:33 | +10 stop | SOL | UP | 0.52 | 0.67 | 1.16 |
| 10-29 23:33 | +10 stop | XRP | UP | 0.55 | 0.66 | 0.76 |
| 10-29 23:33 | +20 | XRP | UP | 0.55 | no | -5.68 |
| 10-29 23:33 | +15 | XRP | UP | 0.55 | no | -5.68 |
| 10-29 23:33 | +10 | XRP | UP | 0.55 | 0.66 | 0.76 |
| 10-29 23:33 | +5 | XRP | UP | 0.55 | 0.66 | 0.76 |
| 10-29 23:33 | +10 stop | BNB | UP | 0.51 | 0.35 | -1.94 |
