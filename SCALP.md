# Range-Scalp Bot

*Updated Sat Nov 28 10:02 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 74495 | 65020 | 9475 (171) | 2 | $-19796.72 | -4.2% |
| **+10¢** | 55495 | 44424 | 11071 (217) | 2 | $-18431.24 | -5.3% |
| **+15¢** | 46467 | 34545 | 11922 (275) | 2 | $-16483.63 | -5.7% |
| **+20¢** | 41347 | 28792 | 12555 (343) | 3 | $-14891.65 | -5.7% |
| **+10¢ (15¢ stop)** | 90658 | 90438 | 220 (136) | 3 | $-33469.44 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-28 10:01 | +10 stop | HYPE | DOWN | 0.71 | open |  |
| 11-28 10:01 | +20 | HYPE | DOWN | 0.71 | open |  |
| 11-28 10:01 | +10 stop | BNB | DOWN | 0.67 | open |  |
| 11-28 10:01 | +20 | BNB | DOWN | 0.67 | open |  |
| 11-28 10:01 | +15 | BNB | DOWN | 0.67 | open |  |
| 11-28 10:01 | +10 | BNB | DOWN | 0.67 | open |  |
| 11-28 10:01 | +5 | BNB | DOWN | 0.67 | open |  |
| 11-28 10:01 | +10 stop | NEAR | DOWN | 0.66 | open |  |
| 11-28 10:01 | +20 | NEAR | DOWN | 0.66 | open |  |
| 11-28 10:01 | +15 | NEAR | DOWN | 0.66 | open |  |
| 11-28 10:01 | +10 | NEAR | DOWN | 0.66 | open |  |
| 11-28 10:01 | +5 | NEAR | DOWN | 0.66 | open |  |
| 11-28 09:58 | +10 stop | DOGE | DOWN | 0.69 | 0.96 | 2.51 |
| 11-28 09:58 | +10 stop | HYPE | DOWN | 0.63 | 0.91 | 2.59 |
| 11-28 09:58 | +20 | HYPE | DOWN | 0.63 | 0.91 | 2.59 |
| 11-28 09:58 | +15 | HYPE | DOWN | 0.63 | 0.91 | 2.59 |
| 11-28 09:58 | +10 | HYPE | DOWN | 0.63 | 0.91 | 2.58 |
| 11-28 09:58 | +5 | HYPE | DOWN | 0.63 | 0.91 | 2.58 |
| 11-28 09:56 | +10 stop | DOGE | DOWN | 0.68 | 0.53 | -1.84 |
| 11-28 09:56 | +5 | ZEC | UP | 0.57 | 0.80 | 2.00 |
| 11-28 09:56 | +10 stop | BTC | UP | 0.63 | 0.82 | 1.62 |
| 11-28 09:56 | +5 | BTC | UP | 0.63 | 0.82 | 1.62 |
| 11-28 09:56 | +10 stop | XRP | UP | 0.50 | 0.84 | 3.12 |
| 11-28 09:54 | +10 stop | DOGE | DOWN | 0.53 | 0.63 | 0.65 |
| 11-28 09:53 | +5 | ZEC | UP | 0.59 | 0.65 | 0.27 |
| 11-28 09:53 | +10 stop | NEAR | DOWN | 0.64 | 0.85 | 1.84 |
| 11-28 09:53 | +20 | NEAR | DOWN | 0.64 | 0.85 | 1.84 |
| 11-28 09:53 | +15 | NEAR | DOWN | 0.64 | 0.85 | 1.84 |
| 11-28 09:53 | +10 | NEAR | DOWN | 0.64 | 0.85 | 1.84 |
| 11-28 09:53 | +5 | NEAR | DOWN | 0.63 | 0.73 | 0.69 |
| 11-28 09:52 | +10 stop | DOGE | DOWN | 0.56 | 0.69 | 0.97 |
| 11-28 09:52 | +10 stop | BTC | UP | 0.68 | 0.80 | 0.92 |
| 11-28 09:52 | +5 | BTC | UP | 0.67 | 0.74 | 0.40 |
| 11-28 09:52 | +10 stop | ZEC | UP | 0.68 | 0.80 | 0.92 |
| 11-28 09:52 | +10 | ZEC | UP | 0.69 | 0.80 | 0.84 |
| 11-28 09:52 | +5 | ZEC | UP | 0.68 | 0.77 | 0.61 |
| 11-28 09:52 | +10 stop | DOGE | DOWN | 0.59 | 0.69 | 0.68 |
| 11-28 09:51 | +5 | XRP | DOWN | 0.65 | yes | -6.65 |
| 11-28 09:50 | +5 | BTC | UP | 0.58 | 0.67 | 0.56 |
| 11-28 09:50 | +10 stop | HYPE | DOWN | 0.68 | 0.78 | 0.71 |
