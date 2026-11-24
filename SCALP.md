# Range-Scalp Bot

*Updated Tue Nov 24 20:37 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 71061 | 62027 | 9034 (155) | 7 | $-18935.69 | -4.2% |
| **+10¢** | 53005 | 42452 | 10553 (201) | 8 | $-17548.88 | -5.3% |
| **+15¢** | 44391 | 33029 | 11362 (258) | 8 | $-15601.09 | -5.6% |
| **+20¢** | 39519 | 27556 | 11963 (324) | 8 | $-13991.27 | -5.6% |
| **+10¢ (15¢ stop)** | 86515 | 86314 | 201 (121) | 2 | $-31819.68 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-24 20:36 | +10 stop | NEAR | UP | 0.50 | 0.24 | -2.91 |
| 11-24 20:36 | +10 stop | BTC | DOWN | 0.68 | open |  |
| 11-24 20:36 | +5 | BTC | DOWN | 0.68 | 0.76 | 0.51 |
| 11-24 20:35 | +10 stop | SOL | UP | 0.52 | 0.35 | -2.04 |
| 11-24 20:34 | +10 stop | XRP | UP | 0.58 | open |  |
| 11-24 20:33 | +10 stop | NEAR | UP | 0.62 | 0.46 | -1.95 |
| 11-24 20:33 | +5 | NEAR | UP | 0.62 | open |  |
| 11-24 20:33 | +10 stop | BNB | DOWN | 0.65 | 0.75 | 0.70 |
| 11-24 20:33 | +10 stop | SOL | DOWN | 0.51 | 0.65 | 1.06 |
| 11-24 20:33 | +10 stop | DOGE | DOWN | 0.62 | 0.80 | 1.51 |
| 11-24 20:33 | +10 stop | XRP | DOWN | 0.69 | 0.54 | -1.83 |
| 11-24 20:33 | +10 stop | ETH | DOWN | 0.65 | 0.75 | 0.70 |
| 11-24 20:32 | +10 stop | BTC | DOWN | 0.66 | 0.76 | 0.71 |
| 11-24 20:32 | +5 | BTC | DOWN | 0.64 | 0.73 | 0.59 |
| 11-24 20:32 | +10 stop | HYPE | UP | 0.51 | 0.24 | -3.01 |
| 11-24 20:32 | +20 | HYPE | UP | 0.51 | open |  |
| 11-24 20:32 | +15 | HYPE | UP | 0.51 | open |  |
| 11-24 20:32 | +10 | HYPE | UP | 0.51 | open |  |
| 11-24 20:32 | +5 | HYPE | UP | 0.51 | open |  |
| 11-24 20:31 | +5 | BTC | UP | 0.55 | 0.62 | 0.35 |
| 11-24 20:31 | +10 stop | ETH | UP | 0.66 | 0.50 | -1.94 |
| 11-24 20:31 | +20 | ETH | UP | 0.66 | open |  |
| 11-24 20:31 | +15 | ETH | UP | 0.66 | open |  |
| 11-24 20:31 | +10 | ETH | UP | 0.66 | open |  |
| 11-24 20:31 | +5 | ETH | UP | 0.66 | open |  |
| 11-24 20:31 | +10 stop | XRP | UP | 0.67 | 0.40 | -3.03 |
| 11-24 20:31 | +20 | XRP | UP | 0.67 | open |  |
| 11-24 20:31 | +15 | XRP | UP | 0.67 | open |  |
| 11-24 20:31 | +10 | XRP | UP | 0.67 | open |  |
| 11-24 20:31 | +5 | XRP | UP | 0.67 | open |  |
| 11-24 20:31 | +10 stop | NEAR | UP | 0.64 | 0.41 | -2.64 |
| 11-24 20:31 | +20 | NEAR | UP | 0.64 | open |  |
| 11-24 20:31 | +15 | NEAR | UP | 0.64 | open |  |
| 11-24 20:31 | +10 | NEAR | UP | 0.64 | open |  |
| 11-24 20:31 | +5 | NEAR | UP | 0.64 | 0.72 | 0.48 |
| 11-24 20:31 | +10 stop | ZEC | UP | 0.58 | 0.42 | -1.96 |
| 11-24 20:31 | +20 | ZEC | UP | 0.58 | 0.78 | 1.69 |
| 11-24 20:31 | +15 | ZEC | UP | 0.58 | 0.76 | 1.49 |
| 11-24 20:31 | +10 | ZEC | UP | 0.58 | 0.76 | 1.49 |
| 11-24 20:31 | +5 | ZEC | UP | 0.58 | 0.64 | 0.25 |
