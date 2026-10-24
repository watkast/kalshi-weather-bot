# Range-Scalp Bot

*Updated Sat Oct 24 12:08 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 31997 | 27891 | 4106 (40) | 2 | $-9190.61 | -4.6% |
| **+10¢** | 23938 | 19192 | 4746 (58) | 2 | $-8195.97 | -5.4% |
| **+15¢** | 20038 | 14936 | 5102 (81) | 2 | $-7326.46 | -5.8% |
| **+20¢** | 17749 | 12409 | 5340 (103) | 2 | $-6504.66 | -5.8% |
| **+10¢ (15¢ stop)** | 39300 | 39241 | 59 (32) | 1 | $-15013.36 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-24 12:07 | +10 stop | BTC | DOWN | 0.62 | open |  |
| 10-24 12:06 | +10 stop | ETH | DOWN | 0.69 | 0.83 | 1.15 |
| 10-24 12:04 | +10 stop | XRP | DOWN | 0.71 | 0.82 | 0.84 |
| 10-24 12:04 | +20 | XRP | DOWN | 0.71 | 0.93 | 1.96 |
| 10-24 12:04 | +15 | XRP | DOWN | 0.71 | 0.86 | 1.26 |
| 10-24 12:04 | +10 | XRP | DOWN | 0.71 | 0.82 | 0.84 |
| 10-24 12:04 | +5 | XRP | DOWN | 0.71 | 0.82 | 0.84 |
| 10-24 12:04 | +10 stop | BTC | UP | 0.58 | 0.40 | -2.15 |
| 10-24 12:04 | +10 | BTC | UP | 0.58 | open |  |
| 10-24 12:04 | +5 | BTC | UP | 0.58 | open |  |
| 10-24 12:04 | +10 stop | ETH | UP | 0.54 | 0.38 | -1.95 |
| 10-24 12:04 | +20 | ETH | UP | 0.54 | open |  |
| 10-24 12:04 | +15 | ETH | UP | 0.53 | open |  |
| 10-24 12:04 | +10 | ETH | UP | 0.53 | open |  |
| 10-24 12:04 | +5 | ETH | UP | 0.53 | open |  |
| 10-24 12:04 | +10 stop | BNB | DOWN | 0.65 | 0.77 | 0.91 |
| 10-24 12:04 | +10 | BNB | DOWN | 0.65 | 0.77 | 0.91 |
| 10-24 12:04 | +5 | BNB | DOWN | 0.65 | 0.77 | 0.91 |
| 10-24 12:04 | +10 stop | SOL | DOWN | 0.69 | 0.79 | 0.73 |
| 10-24 12:04 | +20 | SOL | DOWN | 0.69 | 0.91 | 1.97 |
| 10-24 12:04 | +15 | SOL | DOWN | 0.69 | 0.87 | 1.57 |
| 10-24 12:04 | +10 | SOL | DOWN | 0.69 | 0.79 | 0.73 |
| 10-24 12:04 | +5 | SOL | DOWN | 0.69 | 0.79 | 0.73 |
| 10-24 12:02 | +5 | BTC | DOWN | 0.65 | 0.72 | 0.39 |
| 10-24 12:01 | +10 stop | BTC | DOWN | 0.62 | 0.72 | 0.68 |
| 10-24 12:01 | +20 | BTC | DOWN | 0.62 | open |  |
| 10-24 12:01 | +15 | BTC | DOWN | 0.62 | open |  |
| 10-24 12:01 | +10 | BTC | DOWN | 0.62 | 0.72 | 0.68 |
| 10-24 12:01 | +5 | BTC | DOWN | 0.62 | 0.68 | 0.27 |
| 10-24 12:01 | +10 stop | ETH | DOWN | 0.62 | 0.75 | 0.99 |
| 10-24 12:01 | +20 | ETH | DOWN | 0.62 | 0.82 | 1.72 |
| 10-24 12:01 | +15 | ETH | DOWN | 0.64 | 0.82 | 1.52 |
| 10-24 12:01 | +10 | ETH | DOWN | 0.64 | 0.75 | 0.79 |
| 10-24 12:01 | +5 | ETH | DOWN | 0.64 | 0.69 | 0.18 |
| 10-24 12:01 | +10 stop | HYPE | DOWN | 0.66 | 0.79 | 0.98 |
| 10-24 12:01 | +20 | HYPE | DOWN | 0.66 | 0.88 | 1.92 |
| 10-24 12:01 | +15 | HYPE | DOWN | 0.66 | 0.84 | 1.54 |
| 10-24 12:01 | +10 | HYPE | DOWN | 0.66 | 0.79 | 0.98 |
| 10-24 12:01 | +5 | HYPE | DOWN | 0.66 | 0.75 | 0.56 |
| 10-24 12:01 | +10 stop | BNB | DOWN | 0.67 | 0.77 | 0.71 |
