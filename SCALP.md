# Range-Scalp Bot

*Updated Sat Oct 10 14:03 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 10510 | 9066 | 1444 (22) | 3 | $-3543.89 | -5.3% |
| **+10¢** | 7960 | 6276 | 1684 (36) | 4 | $-3379.60 | -6.7% |
| **+15¢** | 6715 | 4933 | 1782 (52) | 6 | $-2831.84 | -6.7% |
| **+20¢** | 5972 | 4116 | 1856 (66) | 5 | $-2388.42 | -6.4% |
| **+10¢ (15¢ stop)** | 12914 | 12876 | 38 (25) | 4 | $-5062.95 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 14:02 | +15 | BTC | DOWN | 0.71 | open |  |
| 10-10 14:02 | +10 stop | ZEC | DOWN | 0.68 | open |  |
| 10-10 14:02 | +10 stop | BTC | DOWN | 0.65 | 0.80 | 1.22 |
| 10-10 14:02 | +10 | BTC | DOWN | 0.65 | 0.80 | 1.22 |
| 10-10 14:02 | +5 | BTC | DOWN | 0.65 | 0.71 | 0.29 |
| 10-10 14:01 | +10 stop | BNB | UP | 0.55 | open |  |
| 10-10 14:01 | +20 | BNB | UP | 0.55 | open |  |
| 10-10 14:01 | +15 | BNB | UP | 0.55 | open |  |
| 10-10 14:01 | +10 | BNB | UP | 0.55 | open |  |
| 10-10 14:01 | +5 | BNB | UP | 0.55 | open |  |
| 10-10 14:01 | +5 | DOGE | DOWN | 0.69 | open |  |
| 10-10 14:01 | +20 | NEAR | DOWN | 0.71 | open |  |
| 10-10 14:01 | +15 | NEAR | DOWN | 0.71 | open |  |
| 10-10 14:01 | +10 stop | NEAR | DOWN | 0.71 | open |  |
| 10-10 14:01 | +10 | NEAR | DOWN | 0.71 | open |  |
| 10-10 14:01 | +5 | NEAR | DOWN | 0.71 | 0.77 | 0.36 |
| 10-10 14:01 | +10 stop | HYPE | UP | 0.62 | open |  |
| 10-10 14:01 | +20 | HYPE | UP | 0.62 | open |  |
| 10-10 14:01 | +15 | HYPE | UP | 0.62 | open |  |
| 10-10 14:01 | +10 | HYPE | UP | 0.62 | open |  |
| 10-10 14:01 | +5 | HYPE | UP | 0.62 | open |  |
| 10-10 14:01 | +10 stop | BTC | DOWN | 0.47 | 0.61 | 1.05 |
| 10-10 14:01 | +20 | BTC | DOWN | 0.47 | 0.71 | 2.07 |
| 10-10 14:01 | +15 | BTC | DOWN | 0.47 | 0.64 | 1.35 |
| 10-10 14:01 | +10 | BTC | DOWN | 0.47 | 0.61 | 1.05 |
| 10-10 14:01 | +5 | BTC | DOWN | 0.47 | 0.61 | 1.05 |
| 10-10 14:01 | +10 stop | XRP | DOWN | 0.63 | 0.77 | 1.10 |
| 10-10 14:01 | +20 | XRP | DOWN | 0.63 | 0.84 | 1.83 |
| 10-10 14:01 | +15 | XRP | DOWN | 0.63 | 0.78 | 1.20 |
| 10-10 14:01 | +10 | XRP | DOWN | 0.63 | 0.77 | 1.10 |
| 10-10 14:01 | +5 | XRP | DOWN | 0.63 | 0.77 | 1.10 |
| 10-10 14:01 | +10 stop | DOGE | DOWN | 0.63 | 0.73 | 0.69 |
| 10-10 14:01 | +20 | DOGE | DOWN | 0.63 | open |  |
| 10-10 14:01 | +15 | DOGE | DOWN | 0.63 | open |  |
| 10-10 14:01 | +10 | DOGE | DOWN | 0.63 | 0.73 | 0.69 |
| 10-10 14:01 | +5 | DOGE | DOWN | 0.62 | 0.71 | 0.58 |
| 10-10 14:01 | +10 stop | ETH | DOWN | 0.65 | 0.79 | 1.12 |
| 10-10 14:01 | +20 | ETH | DOWN | 0.65 | 0.88 | 2.06 |
| 10-10 14:01 | +15 | ETH | DOWN | 0.65 | 0.88 | 2.06 |
| 10-10 14:01 | +10 | ETH | DOWN | 0.64 | 0.79 | 1.21 |
