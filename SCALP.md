# Range-Scalp Bot

*Updated Wed Oct 21 09:02 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 26934 | 23448 | 3486 (39) | 7 | $-7869.96 | -4.6% |
| **+10¢** | 20268 | 16241 | 4027 (55) | 7 | $-6955.45 | -5.5% |
| **+15¢** | 16971 | 12640 | 4331 (78) | 7 | $-6209.27 | -5.8% |
| **+20¢** | 15027 | 10486 | 4541 (97) | 7 | $-5585.91 | -5.9% |
| **+10¢ (15¢ stop)** | 33022 | 32963 | 59 (32) | 6 | $-12199.64 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 09:02 | +10 stop | DOGE | UP | 0.57 | open |  |
| 10-21 09:02 | +20 | DOGE | UP | 0.57 | open |  |
| 10-21 09:02 | +15 | DOGE | UP | 0.57 | open |  |
| 10-21 09:02 | +10 | DOGE | UP | 0.57 | open |  |
| 10-21 09:02 | +5 | DOGE | UP | 0.57 | open |  |
| 10-21 09:02 | +10 stop | ETH | UP | 0.66 | open |  |
| 10-21 09:02 | +20 | ETH | UP | 0.66 | open |  |
| 10-21 09:02 | +15 | ETH | UP | 0.66 | open |  |
| 10-21 09:02 | +10 | ETH | UP | 0.66 | open |  |
| 10-21 09:02 | +5 | ETH | UP | 0.66 | open |  |
| 10-21 09:02 | +10 stop | BTC | UP | 0.58 | open |  |
| 10-21 09:02 | +20 | BTC | UP | 0.58 | open |  |
| 10-21 09:02 | +15 | BTC | UP | 0.58 | open |  |
| 10-21 09:02 | +10 | BTC | UP | 0.58 | open |  |
| 10-21 09:02 | +5 | BTC | UP | 0.58 | open |  |
| 10-21 09:01 | +10 stop | NEAR | DOWN | 0.59 | 0.41 | -2.14 |
| 10-21 09:01 | +20 | NEAR | DOWN | 0.59 | open |  |
| 10-21 09:01 | +15 | NEAR | DOWN | 0.59 | open |  |
| 10-21 09:01 | +10 | NEAR | DOWN | 0.59 | open |  |
| 10-21 09:01 | +5 | NEAR | DOWN | 0.59 | open |  |
| 10-21 09:01 | +10 stop | XRP | UP | 0.66 | open |  |
| 10-21 09:01 | +20 | XRP | UP | 0.66 | open |  |
| 10-21 09:01 | +15 | XRP | UP | 0.66 | open |  |
| 10-21 09:01 | +10 | XRP | UP | 0.66 | open |  |
| 10-21 09:01 | +5 | XRP | UP | 0.66 | open |  |
| 10-21 09:01 | +10 stop | BNB | DOWN | 0.55 | open |  |
| 10-21 09:01 | +20 | BNB | DOWN | 0.55 | open |  |
| 10-21 09:01 | +15 | BNB | DOWN | 0.54 | open |  |
| 10-21 09:01 | +10 | BNB | DOWN | 0.54 | open |  |
| 10-21 09:01 | +5 | BNB | DOWN | 0.54 | open |  |
| 10-21 09:01 | +10 stop | HYPE | DOWN | 0.68 | open |  |
| 10-21 09:01 | +20 | HYPE | DOWN | 0.68 | open |  |
| 10-21 09:01 | +15 | HYPE | DOWN | 0.68 | open |  |
| 10-21 09:01 | +10 | HYPE | DOWN | 0.68 | open |  |
| 10-21 09:01 | +5 | HYPE | DOWN | 0.68 | open |  |
| 10-21 08:58 | +10 stop | BTC | DOWN | 0.68 | 0.85 | 1.45 |
| 10-21 08:58 | +20 | BTC | DOWN | 0.68 | 0.98 | 2.85 |
| 10-21 08:58 | +15 | BTC | DOWN | 0.67 | 0.85 | 1.55 |
| 10-21 08:58 | +10 | BTC | DOWN | 0.67 | 0.85 | 1.55 |
| 10-21 08:58 | +5 | BTC | DOWN | 0.67 | 0.75 | 0.50 |
