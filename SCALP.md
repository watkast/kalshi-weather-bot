# Range-Scalp Bot

*Updated Thu Nov 19 05:49 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 64839 | 56582 | 8257 (124) | 7 | $-17488.48 | -4.3% |
| **+10¢** | 48437 | 38779 | 9658 (165) | 6 | $-16277.16 | -5.3% |
| **+15¢** | 40617 | 30201 | 10416 (210) | 7 | $-14696.51 | -5.8% |
| **+20¢** | 36168 | 25230 | 10938 (265) | 8 | $-13003.10 | -5.7% |
| **+10¢ (15¢ stop)** | 78880 | 78716 | 164 (98) | 5 | $-28960.98 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-19 05:48 | +5 | SOL | UP | 0.55 | 0.66 | 0.76 |
| 11-19 05:48 | +10 stop | BTC | DOWN | 0.54 | open |  |
| 11-19 05:47 | +10 stop | BNB | DOWN | 0.62 | open |  |
| 11-19 05:47 | +10 stop | HYPE | DOWN | 0.55 | 0.34 | -2.44 |
| 11-19 05:47 | +5 | XRP | DOWN | 0.61 | open |  |
| 11-19 05:47 | +5 | DOGE | DOWN | 0.62 | open |  |
| 11-19 05:47 | +10 stop | ETH | DOWN | 0.62 | open |  |
| 11-19 05:47 | +10 stop | NEAR | DOWN | 0.65 | open |  |
| 11-19 05:47 | +10 stop | XRP | UP | 0.49 | open |  |
| 11-19 05:47 | +20 | XRP | UP | 0.50 | open |  |
| 11-19 05:47 | +15 | XRP | UP | 0.50 | open |  |
| 11-19 05:47 | +10 | XRP | UP | 0.50 | open |  |
| 11-19 05:47 | +5 | XRP | UP | 0.50 | 0.55 | 0.14 |
| 11-19 05:47 | +10 stop | DOGE | UP | 0.47 | 0.60 | 0.95 |
| 11-19 05:47 | +20 | DOGE | UP | 0.47 | open |  |
| 11-19 05:47 | +15 | DOGE | UP | 0.47 | open |  |
| 11-19 05:47 | +10 | DOGE | UP | 0.47 | 0.60 | 0.95 |
| 11-19 05:47 | +5 | DOGE | UP | 0.46 | 0.55 | 0.54 |
| 11-19 05:47 | +10 stop | SOL | UP | 0.51 | 0.66 | 1.16 |
| 11-19 05:47 | +20 | SOL | UP | 0.51 | open |  |
| 11-19 05:47 | +15 | SOL | UP | 0.50 | 0.66 | 1.26 |
| 11-19 05:47 | +10 | SOL | UP | 0.51 | 0.66 | 1.16 |
| 11-19 05:47 | +5 | SOL | UP | 0.51 | 0.56 | 0.14 |
| 11-19 05:46 | +10 stop | HYPE | UP | 0.64 | 0.45 | -2.25 |
| 11-19 05:46 | +20 | HYPE | UP | 0.64 | open |  |
| 11-19 05:46 | +15 | HYPE | UP | 0.64 | open |  |
| 11-19 05:46 | +10 | HYPE | UP | 0.64 | open |  |
| 11-19 05:46 | +5 | HYPE | UP | 0.64 | open |  |
| 11-19 05:46 | +10 stop | BTC | UP | 0.65 | 0.49 | -1.94 |
| 11-19 05:46 | +20 | BTC | UP | 0.65 | open |  |
| 11-19 05:46 | +15 | BTC | UP | 0.65 | open |  |
| 11-19 05:46 | +10 | BTC | UP | 0.65 | open |  |
| 11-19 05:46 | +5 | BTC | UP | 0.66 | open |  |
| 11-19 05:46 | +10 stop | BNB | UP | 0.69 | 0.45 | -2.74 |
| 11-19 05:46 | +20 | BNB | UP | 0.69 | open |  |
| 11-19 05:46 | +15 | BNB | UP | 0.70 | open |  |
| 11-19 05:46 | +10 | BNB | UP | 0.70 | open |  |
| 11-19 05:46 | +5 | BNB | UP | 0.70 | open |  |
| 11-19 05:46 | +10 stop | ETH | UP | 0.65 | 0.49 | -1.94 |
| 11-19 05:46 | +20 | ETH | UP | 0.65 | open |  |
