# Range-Scalp Bot

*Updated Sun Oct 11 02:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 11233 | 9690 | 1543 (22) | 6 | $-3785.01 | -5.3% |
| **+10¢** | 8515 | 6716 | 1799 (36) | 7 | $-3614.02 | -6.7% |
| **+15¢** | 7176 | 5273 | 1903 (52) | 7 | $-3050.12 | -6.8% |
| **+20¢** | 6388 | 4407 | 1981 (66) | 7 | $-2570.61 | -6.4% |
| **+10¢ (15¢ stop)** | 13844 | 13803 | 41 (25) | 7 | $-5547.80 | -6.4% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 02:01 | +10 stop | HYPE | UP | 0.58 | open |  |
| 10-11 02:01 | +20 | HYPE | UP | 0.58 | open |  |
| 10-11 02:01 | +15 | HYPE | UP | 0.57 | open |  |
| 10-11 02:01 | +10 | HYPE | UP | 0.57 | open |  |
| 10-11 02:01 | +5 | HYPE | UP | 0.58 | open |  |
| 10-11 02:01 | +10 stop | SOL | DOWN | 0.62 | open |  |
| 10-11 02:01 | +20 | SOL | DOWN | 0.62 | open |  |
| 10-11 02:01 | +15 | SOL | DOWN | 0.62 | open |  |
| 10-11 02:01 | +10 | SOL | DOWN | 0.62 | open |  |
| 10-11 02:01 | +5 | SOL | DOWN | 0.62 | open |  |
| 10-11 02:01 | +10 stop | DOGE | DOWN | 0.61 | open |  |
| 10-11 02:01 | +20 | DOGE | DOWN | 0.61 | open |  |
| 10-11 02:01 | +15 | DOGE | DOWN | 0.61 | open |  |
| 10-11 02:01 | +10 | DOGE | DOWN | 0.61 | open |  |
| 10-11 02:01 | +5 | DOGE | DOWN | 0.61 | 0.67 | 0.27 |
| 10-11 02:01 | +10 stop | XRP | DOWN | 0.53 | open |  |
| 10-11 02:01 | +20 | XRP | DOWN | 0.53 | open |  |
| 10-11 02:01 | +15 | XRP | DOWN | 0.53 | open |  |
| 10-11 02:01 | +10 | XRP | DOWN | 0.53 | open |  |
| 10-11 02:01 | +5 | XRP | DOWN | 0.53 | open |  |
| 10-11 02:01 | +10 stop | BTC | DOWN | 0.66 | open |  |
| 10-11 02:01 | +20 | BTC | DOWN | 0.66 | open |  |
| 10-11 02:01 | +15 | BTC | DOWN | 0.66 | open |  |
| 10-11 02:01 | +10 | BTC | DOWN | 0.66 | open |  |
| 10-11 02:01 | +5 | BTC | DOWN | 0.66 | open |  |
| 10-11 02:01 | +10 stop | BNB | DOWN | 0.68 | open |  |
| 10-11 02:01 | +20 | BNB | DOWN | 0.68 | open |  |
| 10-11 02:01 | +15 | BNB | DOWN | 0.68 | open |  |
| 10-11 02:01 | +10 | BNB | DOWN | 0.68 | open |  |
| 10-11 02:01 | +5 | BNB | DOWN | 0.68 | open |  |
| 10-11 02:01 | +10 stop | ETH | DOWN | 0.61 | open |  |
| 10-11 02:01 | +20 | ETH | DOWN | 0.61 | open |  |
| 10-11 02:01 | +15 | ETH | DOWN | 0.61 | open |  |
| 10-11 02:01 | +10 | ETH | DOWN | 0.61 | open |  |
| 10-11 02:01 | +5 | ETH | DOWN | 0.61 | open |  |
| 10-11 01:57 | +10 stop | ZEC | DOWN | 0.67 | 0.49 | -2.14 |
| 10-11 01:57 | +10 stop | XRP | UP | 0.67 | 0.84 | 1.44 |
| 10-11 01:56 | +10 stop | XRP | DOWN | 0.29 | 0.65 | 3.29 |
| 10-11 01:56 | +10 stop | ZEC | DOWN | 0.68 | 0.42 | -2.94 |
| 10-11 01:56 | +10 | ZEC | DOWN | 0.68 | yes | -6.96 |
