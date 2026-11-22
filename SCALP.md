# Range-Scalp Bot

*Updated Sun Nov 22 01:08 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 68051 | 59396 | 8655 (138) | 7 | $-18209.18 | -4.3% |
| **+10¢** | 50807 | 40697 | 10110 (181) | 7 | $-16871.53 | -5.3% |
| **+15¢** | 42588 | 31687 | 10901 (230) | 7 | $-15144.01 | -5.7% |
| **+20¢** | 37912 | 26455 | 11457 (288) | 8 | $-13466.69 | -5.7% |
| **+10¢ (15¢ stop)** | 82847 | 82669 | 178 (110) | 5 | $-30417.28 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 01:08 | +10 stop | BTC | UP | 0.51 | open |  |
| 11-22 01:08 | +10 stop | ZEC | DOWN | 0.60 | open |  |
| 11-22 01:07 | +10 stop | ETH | UP | 0.65 | open |  |
| 11-22 01:07 | +10 stop | XRP | UP | 0.71 | open |  |
| 11-22 01:07 | +10 stop | ZEC | UP | 0.42 | 0.65 | 1.96 |
| 11-22 01:07 | +10 stop | DOGE | UP | 0.60 | open |  |
| 11-22 01:06 | +10 stop | ETH | UP | 0.61 | 0.71 | 0.68 |
| 11-22 01:05 | +10 stop | ZEC | DOWN | 0.65 | 0.50 | -1.84 |
| 11-22 01:05 | +5 | ZEC | DOWN | 0.65 | open |  |
| 11-22 01:05 | +5 | DOGE | DOWN | 0.63 | open |  |
| 11-22 01:04 | +10 stop | ZEC | DOWN | 0.56 | 0.71 | 1.17 |
| 11-22 01:04 | +10 stop | BTC | DOWN | 0.59 | 0.44 | -1.85 |
| 11-22 01:04 | +10 stop | SOL | UP | 0.50 | 0.74 | 2.08 |
| 11-22 01:03 | +10 stop | BNB | UP | 0.67 | 0.77 | 0.71 |
| 11-22 01:03 | +10 stop | XRP | UP | 0.59 | 0.70 | 0.78 |
| 11-22 01:03 | +10 stop | NEAR | UP | 0.65 | 0.50 | -1.84 |
| 11-22 01:02 | +10 stop | NEAR | DOWN | 0.70 | 0.51 | -2.23 |
| 11-22 01:02 | +10 stop | DOGE | DOWN | 0.61 | 0.43 | -2.15 |
| 11-22 01:02 | +20 | DOGE | DOWN | 0.61 | open |  |
| 11-22 01:02 | +15 | DOGE | DOWN | 0.61 | open |  |
| 11-22 01:02 | +10 | DOGE | DOWN | 0.61 | open |  |
| 11-22 01:02 | +5 | DOGE | DOWN | 0.61 | 0.66 | 0.17 |
| 11-22 01:02 | +10 stop | BNB | DOWN | 0.57 | 0.37 | -2.35 |
| 11-22 01:02 | +20 | BNB | DOWN | 0.57 | open |  |
| 11-22 01:02 | +15 | BNB | DOWN | 0.57 | open |  |
| 11-22 01:02 | +10 | BNB | DOWN | 0.59 | open |  |
| 11-22 01:02 | +5 | BNB | DOWN | 0.59 | open |  |
| 11-22 01:02 | +10 stop | ETH | DOWN | 0.63 | 0.47 | -1.95 |
| 11-22 01:02 | +20 | ETH | DOWN | 0.63 | open |  |
| 11-22 01:02 | +15 | ETH | DOWN | 0.64 | open |  |
| 11-22 01:02 | +10 | ETH | DOWN | 0.64 | open |  |
| 11-22 01:02 | +5 | ETH | DOWN | 0.64 | open |  |
| 11-22 01:02 | +10 stop | ZEC | DOWN | 0.63 | 0.48 | -1.85 |
| 11-22 01:02 | +20 | ZEC | DOWN | 0.63 | open |  |
| 11-22 01:02 | +15 | ZEC | DOWN | 0.63 | open |  |
| 11-22 01:02 | +10 | ZEC | DOWN | 0.63 | open |  |
| 11-22 01:02 | +5 | ZEC | DOWN | 0.62 | 0.71 | 0.58 |
| 11-22 01:02 | +10 stop | BTC | DOWN | 0.67 | 0.52 | -1.84 |
| 11-22 01:02 | +20 | BTC | DOWN | 0.67 | open |  |
| 11-22 01:02 | +15 | BTC | DOWN | 0.67 | open |  |
