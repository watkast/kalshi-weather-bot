# Range-Scalp Bot

*Updated Sat Oct 24 02:04 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 31260 | 27240 | 4020 (40) | 8 | $-9044.12 | -4.6% |
| **+10¢** | 23392 | 18748 | 4644 (58) | 8 | $-8039.63 | -5.5% |
| **+15¢** | 19571 | 14578 | 4993 (81) | 9 | $-7208.45 | -5.9% |
| **+20¢** | 17340 | 12111 | 5229 (103) | 9 | $-6434.53 | -5.9% |
| **+10¢ (15¢ stop)** | 38352 | 38293 | 59 (32) | 8 | $-14603.03 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-24 02:04 | +10 stop | XRP | UP | 0.66 | open |  |
| 10-24 02:04 | +5 | BNB | UP | 0.59 | open |  |
| 10-24 02:04 | +5 | ETH | UP | 0.58 | open |  |
| 10-24 02:01 | +10 stop | ZEC | DOWN | 0.54 | open |  |
| 10-24 02:01 | +10 | ZEC | DOWN | 0.54 | open |  |
| 10-24 02:01 | +5 | ZEC | DOWN | 0.54 | open |  |
| 10-24 02:01 | +10 stop | HYPE | DOWN | 0.57 | open |  |
| 10-24 02:01 | +10 | HYPE | DOWN | 0.57 | open |  |
| 10-24 02:01 | +5 | HYPE | DOWN | 0.57 | open |  |
| 10-24 02:01 | +10 stop | BTC | DOWN | 0.62 | open |  |
| 10-24 02:01 | +20 | BTC | DOWN | 0.62 | open |  |
| 10-24 02:01 | +15 | BTC | DOWN | 0.62 | open |  |
| 10-24 02:01 | +10 | BTC | DOWN | 0.62 | open |  |
| 10-24 02:01 | +5 | BTC | DOWN | 0.62 | open |  |
| 10-24 02:01 | +5 | DOGE | DOWN | 0.53 | open |  |
| 10-24 02:01 | +10 stop | NEAR | DOWN | 0.63 | open |  |
| 10-24 02:01 | +20 | NEAR | DOWN | 0.63 | open |  |
| 10-24 02:01 | +15 | NEAR | DOWN | 0.63 | open |  |
| 10-24 02:01 | +10 | NEAR | DOWN | 0.63 | open |  |
| 10-24 02:01 | +5 | NEAR | DOWN | 0.63 | 0.72 | 0.58 |
| 10-24 02:01 | +10 stop | SOL | DOWN | 0.64 | open |  |
| 10-24 02:01 | +20 | SOL | DOWN | 0.64 | open |  |
| 10-24 02:01 | +15 | SOL | DOWN | 0.64 | open |  |
| 10-24 02:01 | +10 | SOL | DOWN | 0.64 | open |  |
| 10-24 02:01 | +5 | SOL | DOWN | 0.64 | open |  |
| 10-24 02:01 | +10 stop | XRP | DOWN | 0.61 | 0.45 | -1.95 |
| 10-24 02:01 | +20 | XRP | DOWN | 0.61 | open |  |
| 10-24 02:01 | +15 | XRP | DOWN | 0.61 | open |  |
| 10-24 02:01 | +10 | XRP | DOWN | 0.61 | open |  |
| 10-24 02:01 | +5 | XRP | DOWN | 0.61 | open |  |
| 10-24 02:01 | +10 stop | HYPE | UP | 0.43 | 0.56 | 0.94 |
| 10-24 02:01 | +20 | HYPE | UP | 0.43 | open |  |
| 10-24 02:01 | +15 | HYPE | UP | 0.43 | open |  |
| 10-24 02:01 | +10 | HYPE | UP | 0.44 | 0.56 | 0.84 |
| 10-24 02:01 | +5 | HYPE | UP | 0.44 | 0.56 | 0.84 |
| 10-24 02:01 | +10 stop | DOGE | UP | 0.48 | open |  |
| 10-24 02:01 | +20 | DOGE | UP | 0.48 | open |  |
| 10-24 02:01 | +15 | DOGE | UP | 0.48 | open |  |
| 10-24 02:01 | +10 | DOGE | UP | 0.48 | open |  |
| 10-24 02:01 | +5 | DOGE | UP | 0.48 | 0.55 | 0.34 |
